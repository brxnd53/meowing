import streamlit as st
import math
#st.title("hi")
#st.header("meow")
#st.text("mlup")

st.text("Calculator made by BrandboBoys (AKA Brand)")
st.text("Report bugs to .brxnd. on Discord or message for any questions or suggestions!")
st.subheader("Realm name:")
realm = st.radio("", ["Valley", "Peak", "Colosseum", "Tidal", "Drowned"])
st.text("")
st.text("")

st.subheader("Which block:")
if realm == "Valley":
    mix = st.radio("", ["Sandstone - Red Sandstone Mix", "Red Sandstone - Copper Mix", "Copper - Coal Mix", "Valley Mix"])
    
if realm == "Peak":
    mix = st.radio("", ["Lapis - Amethyst Mix", "Amethyst - Diamond Mix", "Diamond - Emerald Mix", "Peak Mix"])
    
if realm == "Colosseum":
    mix = st.radio("", ["Iron - Redstone Mix", "Redstone - Calcium Mix", "Calcium - Gold Mix", "Colosseum Mix"])
    
if realm == "Tidal":
    mix = st.radio("", ["Tube Coral - Fire Coral Mix", "Fire Coral - Horn Coral Mix", "Horn Coral - Bubble Coral Mix", "Tidal Mix"])
    
if realm == "Drowned":
    mix = st.radio("", ["Seaweed - Sea Floor Mix", "Sea Floor - Foreign Machinery Mix", "Foreign Machinery - Volcanic Rock Mix", "Drowned Mix"])
    
    
st.text("")
blocks = st.text_input("How many blocks:", value="0")
blocks = float(blocks)

if mix == "Sandstone - Red Sandstone Mix":
    block1 = 1 
    block2 = 1
    block1n = "Sandstone"
    block2n = "Red Sandstone"
    
if mix == "Red Sandstone - Copper Mix":
    block1 = 4
    block2 = 4
    block1n = "Red Sandstone"
    block2n = "Copper"
    
if mix == "Copper - Coal Mix":
    block1 = 8
    block2 = 8
    block1n = "Copper"
    block2n = "Coal"
    
if mix == "Valley Mix":
    mixblock1 = 3*4
    mixblockmid1 = 3*4
    mixblockmid2 = 3*8
    mixblock4 = 3*8
    mixblock1n = "Red Sandstone"
    mixblock2n = "Copper"
    mixblock4n = "Coal"
    
    

if mix == "Lapis - Amethyst Mix":
    block1 = 2
    block2 = 3
    block1n = "Lapis"
    block2n = "Amethyst"
    
if mix == "Amethyst - Diamond Mix":
    block1 = 6
    block2 = 5
    block1n = "Amethyst"
    block2n = "Diamond"
    
if mix == "Diamond - Emerald Mix":
    block1 = 10
    block2 = 10
    block1n = "Diamond"
    block2n = "Emerald"
    
if mix == "Peak Mix":
    mixblock1 = 5*6
    mixblockmid1 = 5*5
    mixblockmid2 = 5*10
    mixblock4 = 5*10
    mixblock1n = "Amethyst"
    mixblock2n = "Diamond"
    mixblock4n = "Emerald"
    
    
    
if mix == "Iron - Redstone Mix":
    block1 = 6
    block2 = 6
    block1n = "Iron"
    block2n = "Redstone"
    
if mix == "Redstone - Calcium Mix":
    block1 = 8
    block2 = 7
    block1n = "Redstone"
    block2n = "Calcium"
    
if mix == "Calcium - Gold Mix":
    block1 = 13
    block2 = 13
    block1n = "Calcium"
    block2n = "Gold"
    
if mix == "Colosseum Mix":
    mixblock1 = 7*8
    mixblockmid1 = 7*7
    mixblockmid2 = 7*13
    mixblock4 = 7*13
    mixblock1n = "Redstone"
    mixblock2n = "Calcium"
    mixblock4n = "Gold"
    
    
    
if mix == "Tube Coral - Fire Coral Mix":
    block1 = 7
    block2 = 7
    block1n = "Tube Coral"
    block2n = "Fire Coral"
    
if mix == "Fire Coral - Horn Coral Mix":
    block1 = 10
    block2 = 8
    block1n = "Fire Coral"
    block2n = "Horn Coral"
    
if mix == "Horn Coral - Bubble Coral Mix":
    block1 = 14
    block2 = 14
    block1n = "Horn Coral"
    block2n = "Bubble Coral"
    
if mix == "Tidal Mix":
    mixblock1 = 7*10
    mixblockmid1 = 7*8
    mixblockmid2 = 7*14
    mixblock4 = 7*14
    mixblock1n = "Fire Coral"
    mixblock2n = "Horn Coral"
    mixblock4n = "Bubble Coral"
    
    
    
if mix == "Seaweed - Sea Floor Mix":
    block1 = 9
    block2 = 9 
    block1n = "Seaweed"
    block2n = "Sea Floor"
    
if mix == "Sea Floor - Foreign Machinery Mix":
    block1 = 11
    block2 = 11
    block1n = "Sea Floor"
    block2n = "Foreign Machinery"
    
if mix == "Foreign Machinery - Volcanic Rock Mix":
    block1 = 16
    block2 = 12
    block1n = "Foreign Machinery"
    block2n = "Volcanic Rock"
    
if mix == "Drowned Mix":
    mixblock1 = 10*11
    mixblockmid1 = 10*11
    mixblockmid2 = 10*16
    mixblock4 = 10*12
    mixblock1n = "Sea Floor"
    mixblock2n = "Foreign Machinery"
    mixblock4n = "Volcanic Rock"

    
if mix == ("Valley Mix"):
    mixblock1 = float(mixblock1)
    mixblock2 = float(mixblockmid1)
    mixblock3 = float(mixblockmid2)
    mixblock4 = float(mixblock4)
    mixtotal1 = round(mixblock1 * blocks)
    mixtotalmid1 = round(mixblock2 * blocks)
    mixtotalmid2 = round(mixblock3 * blocks)
    mixtotal4 = round(mixblock4 * blocks)
    mixtotalmid = mixtotalmid1+mixtotalmid2
    mixtotal1stack = math.floor(mixtotal1/64)
    mixtotal1stackleft = mixtotal1-(mixtotal1stack*64)
    mixtotalmidstack = math.floor(mixtotalmid/64)
    mixtotalmidstackleft = mixtotalmid-(mixtotalmidstack*64)
    mixtotal4stack = math.floor(mixtotal4/64)
    mixtotal4stackleft = mixtotal4-(mixtotal4stack*64)
    st.title(f"You need {mixtotal1} T3 {mixblock1n} ({mixtotal1stack} stacks and {mixtotal1stackleft} blocks)")
    st.title(f"You need {mixtotalmid} T3 {mixblock2n} ({mixtotalmidstack} stacks and {mixtotalmidstackleft} blocks)")
    st.title(f"You need {mixtotal4} T3 {mixblock4n} ({mixtotal4stack} stacks and {mixtotal4stackleft} blocks)")
    pass
elif mix == ("Peak Mix"):
    mixblock1 = float(mixblock1)
    mixblock2 = float(mixblockmid1)
    mixblock3 = float(mixblockmid2)
    mixblock4 = float(mixblock4)
    mixtotal1 = round(mixblock1 * blocks)
    mixtotalmid1 = round(mixblock2 * blocks)
    mixtotalmid2 = round(mixblock3 * blocks)
    mixtotal4 = round(mixblock4 * blocks)
    mixtotalmid = mixtotalmid1+mixtotalmid2
    mixtotal1stack = math.floor(mixtotal1/64)
    mixtotal1stackleft = mixtotal1-(mixtotal1stack*64)
    mixtotalmidstack = math.floor(mixtotalmid/64)
    mixtotalmidstackleft = mixtotalmid-(mixtotalmidstack*64)
    mixtotal4stack = math.floor(mixtotal4/64)
    mixtotal4stackleft = mixtotal4-(mixtotal4stack*64)
    st.title(f"You need {mixtotal1} T3 {mixblock1n} ({mixtotal1stack} stacks and {mixtotal1stackleft} blocks)")
    st.title(f"You need {mixtotalmid} T3 {mixblock2n} ({mixtotalmidstack} stacks and {mixtotalmidstackleft} blocks)")
    st.title(f"You need {mixtotal4} T3 {mixblock4n} ({mixtotal4stack} stacks and {mixtotal4stackleft} blocks)")
    pass
elif mix == ("Colosseum Mix"):
    mixblock1 = float(mixblock1)
    mixblock2 = float(mixblockmid1)
    mixblock3 = float(mixblockmid2)
    mixblock4 = float(mixblock4)
    mixtotal1 = round(mixblock1 * blocks)
    mixtotalmid1 = round(mixblock2 * blocks)
    mixtotalmid2 = round(mixblock3 * blocks)
    mixtotal4 = round(mixblock4 * blocks)
    mixtotalmid = mixtotalmid1+mixtotalmid2
    mixtotal1stack = math.floor(mixtotal1/64)
    mixtotal1stackleft = mixtotal1-(mixtotal1stack*64)
    mixtotalmidstack = math.floor(mixtotalmid/64)
    mixtotalmidstackleft = mixtotalmid-(mixtotalmidstack*64)
    mixtotal4stack = math.floor(mixtotal4/64)
    mixtotal4stackleft = mixtotal4-(mixtotal4stack*64)
    st.title(f"You need {mixtotal1} T3 {mixblock1n} ({mixtotal1stack} stacks and {mixtotal1stackleft} blocks)")
    st.title(f"You need {mixtotalmid} T3 {mixblock2n} ({mixtotalmidstack} stacks and {mixtotalmidstackleft} blocks)")
    st.title(f"You need {mixtotal4} T3 {mixblock4n} ({mixtotal4stack} stacks and {mixtotal4stackleft} blocks)")
    pass
elif mix == ("Tidal Mix"):
    mixblock1 = float(mixblock1)
    mixblock2 = float(mixblockmid1)
    mixblock3 = float(mixblockmid2)
    mixblock4 = float(mixblock4)
    mixtotal1 = round(mixblock1 * blocks)
    mixtotalmid1 = round(mixblock2 * blocks)
    mixtotalmid2 = round(mixblock3 * blocks)
    mixtotal4 = round(mixblock4 * blocks)
    mixtotalmid = mixtotalmid1+mixtotalmid2
    mixtotal1stack = math.floor(mixtotal1/64)
    mixtotal1stackleft = mixtotal1-(mixtotal1stack*64)
    mixtotalmidstack = math.floor(mixtotalmid/64)
    mixtotalmidstackleft = mixtotalmid-(mixtotalmidstack*64)
    mixtotal4stack = math.floor(mixtotal4/64)
    mixtotal4stackleft = mixtotal4-(mixtotal4stack*64)
    st.title(f"You need {mixtotal1} T3 {mixblock1n} ({mixtotal1stack} stacks and {mixtotal1stackleft} blocks)")
    st.title(f"You need {mixtotalmid} T3 {mixblock2n} ({mixtotalmidstack} stacks and {mixtotalmidstackleft} blocks)")
    st.title(f"You need {mixtotal4} T3 {mixblock4n} ({mixtotal4stack} stacks and {mixtotal4stackleft} blocks)")
    pass
elif mix == ("Drowned Mix"):
    mixblock1 = float(mixblock1)
    mixblock2 = float(mixblockmid1)
    mixblock3 = float(mixblockmid2)
    mixblock4 = float(mixblock4)
    mixtotal1 = round(mixblock1 * blocks)
    mixtotalmid1 = round(mixblock2 * blocks)
    mixtotalmid2 = round(mixblock3 * blocks)
    mixtotal4 = round(mixblock4 * blocks)
    mixtotalmid = mixtotalmid1+mixtotalmid2
    mixtotal1stack = math.floor(mixtotal1/64)
    mixtotal1stackleft = mixtotal1-(mixtotal1stack*64)
    mixtotalmidstack = math.floor(mixtotalmid/64)
    mixtotalmidstackleft = mixtotalmid-(mixtotalmidstack*64)
    mixtotal4stack = math.floor(mixtotal4/64)
    mixtotal4stackleft = mixtotal4-(mixtotal4stack*64)
    st.title(f"You need {mixtotal1} T3 {mixblock1n} ({mixtotal1stack} stacks and {mixtotal1stackleft} blocks)")
    st.title(f"You need {mixtotalmid} T3 {mixblock2n} ({mixtotalmidstack} stacks and {mixtotalmidstackleft} blocks)")
    st.title(f"You need {mixtotal4} T3 {mixblock4n} ({mixtotal4stack} stacks and {mixtotal4stackleft} blocks)")
    pass
elif mix != ("Valley Mix"):  
    block1 = float(block1)
    block2 = float(block2)
    total1 = round(block1 * blocks)
    total2 = round(block2 * blocks)
    total1stack = math.floor(total1/64)
    total1stackleft = total1-(total1stack*64)
    total2stack = math.floor(total2/64)
    total2stackleft = total1-(total2stack*64)
    st.title(f"You need {total1} T3 {block1n} ({total1stack} stacks and {total1stackleft} blocks)")
    st.title(f"You need {total2} T3 {block2n} ({total2stack} stacks and {total2stackleft} blocks)")
elif mix != ("Peak Mix"):  
    block1 = float(block1)
    block2 = float(block2)
    total1 = round(block1 * blocks)
    total2 = round(block2 * blocks)
    total1stack = math.floor(total1/64)
    total1stackleft = total1-(total1stack*64)
    total2stack = math.floor(total2/64)
    total2stackleft = total1-(total2stack*64)
    st.title(f"You need {total1} T3 {block1n} ({total1stack} stacks and {total1stackleft} blocks)")
    st.title(f"You need {total2} T3 {block2n} ({total2stack} stacks and {total2stackleft} blocks)")
elif mix != ("Colosseum Mix"):  
    block1 = float(block1)
    block2 = float(block2)
    total1 = round(block1 * blocks)
    total2 = round(block2 * blocks)
    total1stack = math.floor(total1/64)
    total1stackleft = total1-(total1stack*64)
    total2stack = math.floor(total2/64)
    total2stackleft = total1-(total2stack*64)
    st.title(f"You need {total1} T3 {block1n} ({total1stack} stacks and {total1stackleft} blocks)")
    st.title(f"You need {total2} T3 {block2n} ({total2stack} stacks and {total2stackleft} blocks)")
elif mix != ("Tidal Mix"):  
    block1 = float(block1)
    block2 = float(block2)
    total1 = round(block1 * blocks)
    total2 = round(block2 * blocks)
    total1stack = math.floor(total1/64)
    total1stackleft = total1-(total1stack*64)
    total2stack = math.floor(total2/64)
    total2stackleft = total1-(total2stack*64)
    st.title(f"You need {total1} T3 {block1n} ({total1stack} stacks and {total1stackleft} blocks)")
    st.title(f"You need {total2} T3 {block2n} ({total2stack} stacks and {total2stackleft} blocks)")
elif mix != ("Drowned Mix"):  
    block1 = float(block1)
    block2 = float(block2)
    total1 = round(block1 * blocks)
    total2 = round(block2 * blocks)
    total1stack = math.floor(total1/64)
    total1stackleft = total1-(total1stack*64)
    total2stack = math.floor(total2/64)
    total2stackleft = total1-(total2stack*64)
    st.title(f"You need {total1} T3 {block1n} ({total1stack} stacks and {total1stackleft} blocks)")
    st.title(f"You need {total2} T3 {block2n} ({total2stack} stacks and {total2stackleft} blocks)")
else:
    pass
