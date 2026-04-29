favourite_languages={
    'Muntaha':'Python',
    'Sidrat':'C++',
    'Amrin':'C',
    'Arian':'JAVA',  
    'Naba':'Ruby', 
}
people=['Muntaha','Amrin','Jen','Shravan','Arian','Rujina']
for name in people:
    print(name.title())
    if name in favourite_languages:
        print("Hello " + name.title() + ", Thank you for responding. I see your favourite language is " + favourite_languages[name].title() + "!")
    else:
        print(f"Hello {name.title()}, I see you haven't taken the poll. Please join us!")
