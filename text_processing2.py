#######################
# Test Processing II  #
#######################



def digits_to_words(input_string):
    digit_eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    dic = dict()
    for i in range(10):
        dic.update({str(i):digit_eng[i]})
        
    temp = []
    for i in input_string:
        if i.isdigit():
            temp.append(dic[i])

    digit_string = ' '.join(temp) 
    
    return digit_string


"""
컴퓨터 프로그래밍에 많은 명명 규칙이 있지만, 두 규칙이 특히 흔히 쓰입니다. 
첫번째로는, 변수 이름을 'underscore'로 나눠준다거나, (ex. under_score_variable)
두번째로는, 변수 이름을 대소문자 구별해 구분자 (delimiter)없이 쓰는 경우가 있습니다. 
이 두번째의 경우에는 첫번째 단어는 소문자로, 그 후에 오는 단어들의 첫번째 글자들은 대문자로 쓰입니다 (ex. camelCaseVariable). 
"""


def to_camel_case(underscore_str):
    underscore_str = ' '.join(underscore_str.strip('_').split('_')).split()

    camelcase_str = ''

    if len(underscore_str) > 1:
        for i in range(len(underscore_str)):
            temp = underscore_str[i].lower()
            
            if i > 0:
                temp = temp[0].upper() + temp[1:]
    
            camelcase_str += temp
    else:
        if underscore_str:
            camelcase_str = ''.join(underscore_str)

    """
    이 문제에서 첫번째 규칙 'underscore variable' 에서 두번째 규칙 'camelcase variable'으로 변환함
    * 앞과 뒤에 여러개의 'underscore'는 무시해도 된
    * 만약 어떤 변수 이름이 underscore로만 이루어 진다면, 빈 문자열만 반환해도 됨

        Parameters:
            underscore_str (string): underscore case를 따른 스트링

        Returns:
            camelcase_str (string): camelcase를 따른 스트링

        Examples:
            >>> import text_processing2 as tp2
            >>> underscore_str1 = "to_camel_case"
            >>> tp2.to_camel_case(underscore_str1)
            "toCamelCase"
            >>> underscore_str2 = "__EXAMPLE__NAME__"
            >>> tp2.to_camel_case(underscore_str2)
            "exampleName"
            >>> underscore_str3 = "alreadyCamel"
            >>> tp2.to_camel_case(underscore_str3)
            "alreadyCamel"
    """

    return camelcase_str
