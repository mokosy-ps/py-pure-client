# list the array's snmp agents
res = client.get_snmp_agents()
print(res)
if type(res) == pypureclient.responses.ValidResponse:
    print(list(res.items))
# Other valid fields: continuation_token, filter, ids, limit, names, offset, sort
# See section "Common Fields" for examples
