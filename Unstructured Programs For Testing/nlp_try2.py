import re
def remove_regex(input_text,regex_patern):
    urls=re.finditer(regex_patern,input_text)
    for i in urls:
        input_text=re.sub(i.group().strip(),'',input_text)
    return input_text

regex_patern="#[\w]*"

print(remove_regex("remove this #hashtag from this line",regex_patern))

