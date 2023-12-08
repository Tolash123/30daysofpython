# Day-16 of #30daysofpython

## Slice Operator

Syntax:
string[Begin:end]------------>(Begin Index to end-1)
string[Begin : end : step]
step can be positive or Negative Index
If step is positive:
Forward Direction
from [begin to end-1]
If step is Negative:
Backward Direction
from [begin to end+1]
step value cannot be zero
NOTE:
In forward direction, if end value is '0' then result is always empty
In backward direction, if end value is '-1' then result is empty
Slice Operator doesn't raise index error
In Forward Direction,
Begin = 0
End = length(string)
In Backward Direction,
Begin = -1
End = -[length(string) + 1]