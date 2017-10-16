-- noinspection SqlDialectInspectionForFile
-- These views provide a simpler interface for viewing Dexter data.

-- document_sources_view:
--   aggregate all information on document sources
create or replace view document_sources_view as
select
  ds.source_type as `source_type`,
  if(ds.unnamed = 1, '(unnamed)', if(p.id is not null, p.name, ds.name)) as `source_name`,
  if(gender_person.id is not null, gender_person.name, gender_unnamed.name) as `gender`,
  if(race_person.id is not null, race_person.name, race_unnamed.name) as `race`,
  sa.name as `source_age`,
  a.name as `affiliation`,
  a.code as `affiliation_code`,
  -- affiliation parent
  ap.name as `affiliation_group`,
  ap.code as `affiliation_group_code`,
  sf.name as `function`,
  sr.name as `role`,
  case ds.quoted when 1 then 'quoted' when 0 then 'not-quoted' end as `quoted`,
  case ds.photographed when 1 then 'photographed' when 0 then 'not-photographed' end as `photographed`,
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
  left join source_roles sr on ds.source_role_id = sr.id
  left join source_ages sa on ds.source_age_id = sa.id
  left join affiliations ap on ap.code = substring_index(a.code, '.', 1)
;

-- person_utterances_view:
--   aggregate all utterances from document source people
create or replace view person_utterances_view as
select
  ds.source_type as `source_type`,
  p.name as `person`,
  r.name as `race`,
  g.name as `gender`,
  sa.name as `source_age`,
  a.name as `affiliation`,
  a.code as `affiliation_code`,
  -- affiliation parent
  ap.name as `affiliation_group`,
  ap.code as `affiliation_group_code`,
  sf.name as `function`,
  sr.name as `role`,
  u.quote,
  p.id as `person_id`,
  ds.doc_id as `document_id`,
  ds.id as `document_source_id`
from
  document_sources ds
  inner join people p on ds.person_id = p.id
  inner join entities e on e.person_id = p.id
  inner join utterances u on u.doc_id = ds.doc_id and u.entity_id = e.id
  left join genders g on p.gender_id = g.id
  left join races r on p.race_id = r.id
  left join affiliations a on ds.affiliation_id = a.id
  left join source_functions sf on ds.source_function_id = sf.id
  left join source_roles sr on ds.source_role_id = sr.id
  left join source_ages sa on ds.source_age_id = sa.id
  left join affiliations ap on ap.code = substring_index(a.code, '.', 1)
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
  c.name as `country`,
  d.item_num as `item_num`,
  m.name as `medium`,
  m.medium_type as `medium_type`,
  if(m.medium_group IS NULL OR m.medium_group = '', m.name, m.medium_group) as `medium_group`,
  if(m.parent_org IS NULL OR m.parent_org = '', m.name, m.parent_org) as `parent_org`,
  t.name as `topic`,
  t.group as `topic_group`,
  l.name as `origin`,
  if(l.group IS NULL or l.group = '', l.name, l.group) as `origin_group`,
  dt.name as `document_type`,
  if (a.person_id is null, a.name, ap.name) as `author_name`,
  at.name as `author_type`,
  d.word_count as `word_count`,
  case d.quality_basic_context when 1 then 'basic-context' when 0 then 'no-basic-context' end as `basic_context`,
  case d.quality_causes when 1 then 'causes-mentioned' when 0 then 'no-causes-mentioned' end as `causes_mentioned`,
  case d.quality_consequences when 1 then 'consequences-mentioned' when 0 then 'no-consequences-mentioned' end as `consequences_mentioned`,
  case d.quality_solutions when 1 then 'solutions-offered' when 0 then 'no-solutions-offered' end as `solutions_offered`,
  case d.quality_policies when 1 then 'relevant-policies' when 0 then 'no-relevant-policies' end as `relevant_policies`,
  case d.quality_self_help when 1 then 'self-help-offered' when 0 then 'no-self-help-offered' end as `self_help_offered`,
  an.name as `analysis_nature`,
  d.flagged as `flagged`,
  if(d.flagged = 1, d.notes, null) as `flag_notes`
from
  documents d
  inner join analysis_natures an on d.analysis_nature_id = an.id
  left join document_types dt on d.document_type_id = dt.id
  left join mediums m on d.medium_id = m.id
  left join topics t on d.topic_id = t.id
  left join locations l on d.origin_location_id = l.id
  left join authors a on d.author_id = a.id
  left join people ap on a.person_id = ap.id
  left join author_types at on a.author_type_id = at.id
  left join users created_user on d.created_by_user_id = created_user.id
  left join users analysis_user on d.checked_by_user_id = analysis_user.id
  left join countries c on d.country_id = c.id
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


-- documents_principles_view:
--   principles for documents
create or replace view documents_principles_view as
select 
  d.id as `document_id`,
  ps.name as `principle_supported`,
  pv.name as `principle_violated`
from
  documents d
  left join principles ps on ps.id = d.principle_supported_id
  left join principles pv on pv.id = d.principle_violated_id
where
  pv.id is not null or ps.id is not null
;


-- documents_places_view:
--   places for documents
create or replace view documents_places_view as
select
  dp.doc_id as `document_id`,
  p.province_code as `province_code`,
  p.province_name as `province_name`,
  p.municipality_code as `municipality_code`,
  p.municipality_name as `municipality_name`,
  p.level,
  case p.level
  when 'province' then p.province_name
  when 'municipality' then p.municipality_name
  when 'mainplace' then p.mainplace_name
  when 'subplace' then p.subplace_name
  end as `name`
from
  document_places dp
  inner join places p on dp.place_id = p.id
where
  dp.relevant = 1
;


-- documents_children_view:
--   child-focused document analysis
create or replace view documents_children_view as
select
  d.id as `document_id`,
  case d.child_focus when 1 then 'child-focused' when 0 then 'not-child-focused' end as `child_focused`,
  case d.abuse_source when 1 then 'secondary-victim-source' when 0 then 'not-secondary-victim-source' end as `secondary_victim_source`,
  case d.abuse_identified when 1 then 'secondary-victim-identified' when 0 then 'not-secondary-victim-identified' end as `secondary_victim_identified`,
  case d.abuse_victim when 1 then 'secondary-victim-abused' when 0 then 'not-secondary-victim-abused' end as `secondary_victim_victim_of_abuse`,
  -- all three abuse settings are true
  if(d.abuse_source = 1 AND
     d.abuse_identified = 1 AND
     d.abuse_victim = 1, 'secondary-victim-source-identified-abused', NULL) as `secondary_victim_source_identified_abused`,
  case d.quality_basic_context when 1 then 'basic-context' when 0 then 'no-basic-context' end as `basic_context`,
  case d.quality_causes when 1 then 'causes-mentioned' when 0 then 'no-causes-mentioned' end as `causes_mentioned`,
  case d.quality_consequences when 1 then 'consequences-mentioned' when 0 then 'no-consequences-mentioned' end as `consequences_mentioned`,
  case d.quality_solutions when 1 then 'solutions-offered' when 0 then 'no-solutions-offered' end as `solutions_offered`,
  case d.quality_policies when 1 then 'relevant-policies' when 0 then 'no-relevant-policies' end as `relevant_policies`,
  case d.quality_self_help when 1 then 'self-help-offered' when 0 then 'no-self-help-offered' end as `self_help_offered`
from
  documents d
  inner join analysis_natures an on d.analysis_nature_id = an.id
where
  an.nature = 'children'
;

-- documents_keywords_view:
--   keywords for all documents (there can be multiple keywords for the same document)
create or replace view documents_keywords_view as
select
  d.id as `document_id`,
  dk.keyword as `keyword`,
  dk.relevance as `relevance`,
  -- number of occurrences
  if(dk.offset_list is null or dk.offset_list = '', 1, length(dk.offset_list) - length(replace(dk.offset_list, ' ', ''))+1) as `occurrences`
from
  documents d
  left join document_keywords dk on dk.doc_id = d.id
;

-- documents_taxonomies_view:
--   taxonomies for all documents (there can be multiple taxonomies for the same document)
create or replace view documents_taxonomies_view as
select
  d.id as `document_id`,
  dt.label as `label`,
  dt.score
from
  documents d
  left join document_taxonomies dt on dt.doc_id = d.id
;

-- investments_view:
--   aggregate scalar information for all investments
create or replace view investments_view as select
  d.name as investment_name,
  date_format(doc.published_at, '%Y/%m/%d') as `published_at`,
  date_format(d.investment_begin, '%Y/%m/%d') as `start_date`,
  date_format(d.investment_end, '%Y/%m/%d') as `end_date`,
  concat(d.value,' ',vu.name,' ',cu.name) as `value`,
  concat('R', d.value2, ' ', vu2.name) as value_rand,
  d.perm_opps,
  d.temp_opps,
  inv1.name,
  inv2.name,
  inv3.name,
  d.company,
  type.name as type,
  p.name as phase,
  date_format(d.phase_date, '%Y/%m/%d') as `phase_date`,
  o.name as origin_of_investment,
  d.invest_origin_city as investment_origin_city,
  s.name as sector_name,
  loc.name as location,
  d.fdi_notes as notes,
  d.doc_id as `document_id`,
  d.id as `investment_id`
from
  investments d
  left join documents doc on d.doc_id = doc.id
  left join involvements1 inv1 on d.involvement_id1 = inv1.id
  left join involvements2 inv2 on d.involvement_id2 = inv2.id
  left join involvements3 inv3 on d.involvement_id3 = inv3.id
  left join value_units vu on d.value_unit_id = vu.id
  left join value_units vu2 on d.value_unit_id2 = vu2.id
  left join currencies cu on d.currency_id = cu.id
  left join investment_types type on d.invest_type_id = type.id
  left join phases p on d.phase_id = p.id
  left join investment_origins o on d.invest_origin_id = o.id
  left join sectors s on d.sector_id = s.id
  left join locations loc on d.invest_loc_id = loc.id
;