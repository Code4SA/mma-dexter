-- These views provide a simpler interface for viewing Dexter data.

-- document_sources_view:
--   aggregate all information on document sources
create or replace view document_sources_view as
select
  if(ds.unnamed = 1, '(unnamed)', if(p.id is not null, p.name, ds.name)) as `source_name`,
  if(gender_person.id is not null, gender_person.name, gender_unnamed.name) as `gender`,
  if(race_person.id is not null, race_person.name, race_unnamed.name) as `race`,
  a.name as `affiliation`,
  a.code as `affiliation_code`,
  sf.name as `function`,
  ds.quoted as `quoted`,
  ds.doc_id as `document_id`,
  ds.id as `document_source_id`
from
  document_sources ds
  left join affiliations a on ds.affiliation_id = a.id
  left join people p on ds.person_id = p.id
  left join genders gender_person on p.gender_id = gender_person.id
  left join genders gender_unnamed on ds.unnamed_gender_id = gender_unnamed.id
  left join races race_person on p.race_id = race_person.id
  left join races race_unnamed on ds.unnamed_race_id = race_unnamed.id
  left join source_functions sf on ds.source_function_id = sf.id
;

-- documents_view:
--   aggregate scalar information for all documents
create or replace view documents_view as select 
  d.id as `document_id`,
  d.url as `article_url`,
  d.title,
  d.published_at as `published_at`,
  date_format(d.published_at, '%Y/%m/%d') as `published_date`,
  concat(created_user.first_name, ' ', created_user.last_name) as `user_added`,
  concat(analysis_user.first_name, ' ', analysis_user.last_name) as `user_analysis`,
  concat('https://mma-dexter.code4sa.org/articles/', d.id) as `dexter_url`,
  d.item_num as `item_num`,
  m.name as `medium`,
  m.medium_type as `medium_type`,
  if(m.medium_group IS NULL OR m.medium_group = '', m.name, m.medium_group) as `medium_group`,
  t.name as `topic`,
  l.name as `origin`,
  if (a.person_id is null, a.name, ap.name) as `author_name`,
  at.name as `author_type`
from
  documents d
  left join mediums m on d.medium_id = m.id
  left join topics t on d.topic_id = t.id
  left join locations l on d.origin_location_id = l.id
  left join authors a on d.author_id = a.id
  left join people ap on a.person_id = ap.id
  left join author_types at on a.author_type_id = at.id
  left join users created_user on d.created_by_user_id = created_user.id
  left join users analysis_user on d.checked_by_user_id = analysis_user.id
;

-- documents_issues_view:
--   issues for all documents (there can be multiple issues for the same document)
create or replace view documents_issues_view as
select 
  d.id as `document_id`,
  i.name as `issue`
from
  documents d
  left join document_issues di on di.doc_id = d.id
  left join issues i on di.issue_id = i.id
;


-- documents_fairness_view:
--   fairness for documents (there can be multiple fairness entries for the same document)
create or replace view documents_fairness_view as
select 
  d.id as `document_id`,
  ifnull(f.name, 'Fair') as `fairness`,
  af_favour.name as `favour`,
  af_favour.code as `favour_code`,
  af_oppose.name as `oppose`,
  af_oppose.code as `oppose_code`
from
  documents d
  left join document_fairness df on df.doc_id = d.id
  left join fairness f on df.fairness_id = f.id
  left join affiliations af_favour on df.bias_favour_affiliation_id = af_favour.id
  left join affiliations af_oppose on df.bias_oppose_affiliation_id = af_oppose.id
;
