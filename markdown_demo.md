# 示例

# 标题

**粗体**

- 缩进
  - 缩进

行内高亮： `markdown`

按键：CTRL

> 多层引用
> > 多层引用

———— 

> 单层引用
> 单层引用

| 表格 | 表格 |
| -    |  -   |
| 表格 | 表格 |


图片： ![图片](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1567699342470&di=a82e9638e3210cb91ec6de8435c98dc2&imgtype=0&src=http%3A%2F%2Fimglf1.ph.126.net%2FEL41V1hr6QzSsKaaccug4Q%3D%3D%2F6630935824305511510.jpg)



代码高亮：
```python
def dict_recursion(dict_all):
    if isinstance(dict_all, dict):
        for x in dict_all:
            dict_key = x
            dict_value = dict_all[dict_key]
            print("{}:{}".format(dict_key, dict_value))
            dict_recursion(dict_value)
    else:
        return
```