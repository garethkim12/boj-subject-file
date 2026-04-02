add_part_list = input().split('-')

# 첫번쨰 괄호를 계산하여 계산
result =sum(map(int, add_part_list[0].split('+')))

# 두번쨰 괄호를 계산해서 빼줌
for add_part in add_part_list[1:]:
    part_result = sum(map(int, add_part.split('+')))
    result -= part_result


print(result)