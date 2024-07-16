def wordcount(text):
    # 根据空格将文本拆分为单词
    words = text.split()
    
    # 创建一个空字典来存储单词计数
    count_dict = {}
    
    # 遍历列表中的每个单词
    for word in words:
        # 从单词中去除标点符号
        word = word.strip('.,!?')
        # 将单词转换为小写以进行不区分大小写的计数
        word = word.lower()
        
        # 如果单词已经在字典中，增加其计数
        if word in count_dict:
            count_dict[word] += 1
        # 否则，将单词添加到字典中，计数为1
        else:
            count_dict[word] = 1
            
    return count_dict

# 使用提供的文本测试函数
text = "Hello world! This is an example. Word count is fun. Is it fun to count words? Yes, it is fun!"
wordcount_result = wordcount(text)
wordcount_result
