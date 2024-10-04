areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

# Delete the poolhouse items from the list
del areas[10]
del areas[10]
#在 Python 列表中，del 操作使用的切片范围是左闭右开的。
# 这意味着开始的索引是包含的（即 10），但结束的索引是
# 不包含的（即结束位置索引 12 不会被删除）。
# 这就是为什么要写成 del areas[10:12]。
# del areas[10:12] 

# Print the updated list
print(areas)