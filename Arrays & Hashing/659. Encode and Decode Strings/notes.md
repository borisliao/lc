### [659. Encode and Decode Strings](https://neetcode.io/problems/string-encode-and-decode)

#Medium #Blind75 #NeetCode150

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement `encode` and `decode`

## Example

**Example 1**

> **Input:** ["leet","code","love","you"]  
> **Output:** ["leet","code","love","you"]  
> **Explanation:** One possible encode method is: "leet:;code:;love:;you"

**Example 2**

> **Input:** ["we", "say", ":", "yes"]  
> **Output:** ["we", "say", ":", "yes"]  
> **Explanation:** One possible encode method is: "we:;say:;:::;yes"

**Constraints:**

- `0 <= strs.length < 100`
- `0 <= strs[i].length < 200`
- `strs[i]` contains only UTF-8 characters.
