sub_specialty_sql = """
        select 
        d.system_name, count(*) as count
        from t_case_sample a
        left join t_dict_sample b on a.sample_id = b.sample_id
        left join t_dict_organ c on a.organ_id = c.organ_id
        left join t_dict_system d on d.system_id = c.system_id
        where a.is_delete=0 {condition} group by d.system_name
"""

total_income_sql = """
        select
        sum(d.site_amount) as total_income
        from t_case a
        left join t_money_config_business_site d on d.site_id = a.site_id and d.business_type_id=a.business_type_id
        where is_delete=0 {condition}
"""

site_dynamics_cast_sql = """
SELECT b.site_name as name,
    SUM(if(case_type=1,1,0)) tissue_count,
    SUM(if(case_type=2,1,0)) cell_count,
    SUM(if(case_type=3,1,0)) frost_count
    from t_case a
    inner join t_site b on a.site_id=b.site_id
    where a.is_delete=0 {condition}
    GROUP BY a.site_id order by a.site_id
"""

site_dynamics_advice_sql = """
SELECT b.site_name as name,
    Count(1) immunostaining_count
    from t_advice a
    inner join t_site b on a.site_id=b.site_id
    where a.is_delete=0 {condition}
    GROUP BY a.site_id order by a.site_id
"""

site_dynamics_molecular_sql = """
SELECT b.site_name as name,
    Count(1) numerator_count
    from t_molecular a
    inner join t_site b on a.site_id=b.site_id
    where a.is_delete=0 {condition}
    GROUP BY a.site_id order by a.site_id
"""