context = {
    'organization': [
        {
            'id': 1,
            'name': 'Test Organization 1',
            'phone': '987654321',
            'email': 'testOrgEmail@gmail.com',
            'address': 'Test Location',
            'status': False,
            'fund_raised': '0',
        },
        {
            'id': 2,
            'name': 'Test Organization 2',
            'phone': '987654321',
            'email': 'testOrgEmail@gmail.com',
            'address': 'Test Location',
            'status': False,
            'fund_raised': '0',
        }
    ]
}
# print(type(context['organization'][0]['id']))
# print(context['organization'][1]['id'])
# print(context['organization'][1]['name'])



arr = [1,2,3]
# for i in arr:
#     print(i)




for dictionary in context['organization']:
    # print(dictionary.keys())
    
    for key in dictionary.keys():
        print(key)
        # key : 'id'
        # 1 

        # key = 'name'
        # 'Test Organization 1'
        print(dictionary[key])




