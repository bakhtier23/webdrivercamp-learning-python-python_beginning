#!/usr/bin/python3

variable = "There should be one-- and preferably only one --obvious way to do it. lthough that way may not be obvious at first unless you're Dutch."
start_index = variable.find("one-- and ") + len("one-- and ")
end_index = variable.find(" --obvious")
preferably_one_way = variable[start_index:end_index]
start_unless = variable.find("unless")
unless_str = " " + variable[start_unless:start_unless + len("unless")]
result = preferably_one_way + unless_str
print(result)
