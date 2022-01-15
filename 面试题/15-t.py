"""
    1、完整语法（语法级别关键字的排列顺序如下）
    select distinct 字段1,字段2,字段3,... from 库名.表名
        where 约束条件
        group by 分组依据
        having 过滤条件
        order by 排序字段
        limit 限制显示的条数
        ;
        
    2、关键词执行的优先级
    from
    where 约束条件
    group by 分组依据
    having 过滤条件
    distinct 去重
    order by 排序的字段
    limit 限制显示的条数

"""