# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
#type(var_name) returns the data type name in a string

### numbers
age = 20;
weight = 67.5;
complicated = 2j;
print("Numeric data types****");
print("\t20 type", type(age));
print("\t67.5 type", type(weight));
print("\t2j type", type(complicated));
### casting
print("Casting data types****");

a1 = str(age);
a2 = int (weight);
a3 =  float("23");
