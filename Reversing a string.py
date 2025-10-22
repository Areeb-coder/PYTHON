s1=input("Enter the 1st word:")
s2=input("Enter the 2nd word:")
s3=s2[::-1]#string slicing
if s1==s3:
    print("They are Palindrome")
else:
    print("Thay are not Palindrome")
    

"""2.Using reversed() built-in function
 Works for any sequence (like string, list, tuple)"""

s = "hello"
rev = ''.join(reversed(s))
print(rev)   # Output: olleh

"""3. Using a loop (manual reversal)

Good for learning loops and conditionals:"""

s = "hello"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)   # Output: olleh

"""4. Using recursion (advanced way)"""
def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]

print(reverse("hello"))  # Output: olleh
