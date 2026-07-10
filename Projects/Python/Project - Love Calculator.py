import random
name1 = input("ENTER YOUR NAME : ")
name2 = input("ENTER YOUR PARTNER'S NAME : ")

user = name1[:3]+ name2[:3]
print(user)

love = random.randint(1, 100)
if love < 10 :
    print(f" {love}% ⤳ 𝒜𝓌𝒻𝓊𝓁")
elif love < 30 :
    print(f" {love}% ⤳ 𝒫𝑜𝑜𝓇")
elif love < 50 :
    print(f" {love}% ⤳ 𝒜𝓋𝑒𝓇𝒶𝑔𝑒")
elif love < 70 :
    print(f" {love}% ⤳ 𝒢𝑜𝑜𝒹")
elif love < 90 :
    print(f" {love}% ⤳ 𝐸𝓍𝒸𝑒𝓁𝓁𝑒𝓃𝓉")
else :
    print(f" {love}% ⤳ 𝑀𝒶𝒹𝑒 𝒻𝑜𝓇 𝐸𝒶𝒸𝒽 𝒪𝓉𝒽𝑒𝓇")


# def calculate_love_score(name1,name2) :
#     combine = name1 + name2
#     combine = combine.upper()
#     count_true = 0
#     count_love = 0
#     for i in "TRUE" :
#         count_true += combine.count(i)
#
#     for i in "LOVE" :
#         count_love += combine.count(i)
#
#     love_score = int(str(count_true) + str(count_love))
#     print(f"YOUR LOVE SCORE IS : {love_score}")
#
#
# calculate_love_score("Kanye West", "Kim Kardashian")




