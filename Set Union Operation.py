english_subscriber=int(input())
english_subscriber_list=set(map(int,input().split()))
french_subscriber=int(input())
french_subscriber_list=set(map(int,input().split()))
only_english_subscriber=english_subscriber_list.union(french_subscriber_list)
print(len(only_english_subscriber))
