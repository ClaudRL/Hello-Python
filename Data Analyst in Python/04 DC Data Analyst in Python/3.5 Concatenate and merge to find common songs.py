# Exercise
# Concatenate and merge to find common songs
# The senior leadership of the streaming service is requesting your help again. You are given the historical files for a popular playlist in the classical music genre in 2018 and 2019. Additionally, you are given a similar set of files for the most popular pop music genre playlist on the streaming service in 2018 and 2019. Your goal is to concatenate the respective files to make a large classical playlist table and overall popular music table. Then filter the classical music table using a semi join to return only the most popular classical music tracks.

# The tables classic_18, classic_19, and pop_18, pop_19 have been loaded for you. Additionally, pandas has been loaded as pd.
# 1. Concatenate the classic_18 and classic_19 tables vertically where the index goes from 0 to n-1, and save to classic_18_19.
# Concatenate the pop_18 and pop_19 tables vertically where the index goes from 0 to n-1, and save to pop_18_19.

# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18,classic_19],ignore_index = True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index = True)

# 2. With classic_18_19 on the left, merge it with pop_18_19 on tid using an inner join.
# Use .isin() to filter classic_18_19 where tid is in classic_pop.

# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19, on = 'tid')

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# Print popular chart
print(popular_classic)



这段代码旨在合并2018和2019年两个音乐流派的播放列表，并筛选出流行且属于古典音乐的曲目。以下是逐行解释：

### 第1部分：合并 2018 和 2019 年的古典和流行音乐表
```python
# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)
```
1. **`pd.concat([classic_18, classic_19], ignore_index=True)`**: 将 `classic_18` 和 `classic_19` 两个古典音乐的表垂直拼接在一起，形成一个新的表 `classic_18_19`。
   - **`ignore_index=True`** 参数将拼接后的新表索引从 0 开始重新编号，确保拼接后的索引不重复。

```python
# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)
```
2. **`pd.concat([pop_18, pop_19], ignore_index=True)`**: 类似地，将流行音乐表 `pop_18` 和 `pop_19` 垂直拼接，生成新表 `pop_18_19`，并重新编号索引。

### 第2部分：使用内连接合并古典和流行音乐表
```python
# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19, on='tid')
```
3. **`classic_18_19.merge(pop_18_19, on='tid')`**: 使用内连接（`inner join`），以 `tid` （歌曲ID）为键，将古典音乐表 `classic_18_19` 与流行音乐表 `pop_18_19` 合并。结果保存在 `classic_pop` 中。
   - **`tid`** 是歌曲的唯一标识符。内连接将只保留那些在两个表中都存在的 `tid`，即流行且属于古典音乐的歌曲。

### 第3部分：过滤出流行的古典音乐曲目
```python
# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]
```
4. **`classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]`**: 使用 `isin()` 方法，过滤 `classic_18_19` 表中的 `tid`，只保留那些出现在 `classic_pop` 表中的 `tid`，即那些同时在古典音乐和流行音乐中流行的歌曲。结果保存在 `popular_classic` 中。

### 最后输出：
```python
# Print popular chart
print(popular_classic)
```
5. **`print(popular_classic)`**: 打印最终的 `popular_classic` 表，展示同时出现在古典和流行音乐表中的曲目。

### 总结：
- 代码首先垂直拼接了古典音乐和流行音乐2018、2019年的表格。
- 然后通过内连接筛选出两种表中共同的 `tid`，即流行的古典音乐曲目。
- 最后通过 `isin()` 方法过滤出古典音乐表中流行的曲目并打印出来。