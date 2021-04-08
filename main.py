# init
print ('loading...')
f = open('sajjad_translate/translate.txt')
big_text = f.read()
parts = big_text.split('\n')
words = []
i = 0
print(len(parts))

while i < len(parts):
    my_dict ={'english':parts[i],'persian':parts[i+1] }   
    words.append(my_dict)
    i +=2

#process
print('data loaded')
print('welcome dear user','please enter your text')

while True:
        print('\n 1-translation eng to per','\n 2-translation per to eng','\n 3-add new word' ,'\n 4-Exit')

        b = int(input())

        if b == 1:
            user_string =input()
            user_words=user_string.split(' ')

            for j in range(len(user_words)):
                for i in range(len(words)):
                    if words[i]['english'] == user_words[j]: # word found
                        print(words[i]['persian'],end=' ')
                        break

                else: # word not found
                    print(user_words[j] , end =' ') 


        elif b == 2:
            user_string =input()
            user_words=user_string.split(' ')

            for j in range(len(user_words)):
                for i in range(len(words)):
                    if words[i]['persian'] == user_words[j]: # word found
                        print(words[i]['english'],end=' ')
                        break

                else: # word not found
                    print(user_words[j] , end =' ')


        elif b == 3:
            eng = input('English = ')
            per = input('Persian = ')
            my_dict ={'english': eng ,'persian':per}   
            words.append(my_dict)
            f = open('sajjad_translate/translate.txt','b') 
            f.write('\n + eng')
            f.write('\n + per')
            f.close()
            print('Done!')

        
        elif b == 4:
            exit()











            
                
            
            