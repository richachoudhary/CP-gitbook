# Adhoc

### \#\#\# --\[CP :: Adhoc\] --\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#

* [x] [1368A. A. C+=](https://codeforces.com/contest/1368/problem/A)
* [ ] 
{% tabs %}
{% tab title="1368A" %}
```python
for _ in range(T):
    a,b,n = I()
    if a>b:
        a,b = b,a
    ans = 0
    while a<= n and b<=n:
        a += b
        a,b = b,a
        ans += 1
    print(ans)
```
{% endtab %}
{% endtabs %}

## 

