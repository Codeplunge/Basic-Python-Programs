def anti_vowel(text):
  x=0
  while x<len(text):
    if text[x] in "aeiouAEIOU":
      text=text[:x]+text[x+1:]
      x-=1
    x+=1
  return text
