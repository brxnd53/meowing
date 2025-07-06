import streamlit as st
import math


st.text("Calculator made by BrandboBoys (AKA Brand)")
st.text("Report bugs to .brxnd. on Discord and message for any questions or suggestions!")

col1, col2 = st.columns(2)


with col1:
    st.subheader("Realm name:")
    realm = st.radio("", ["Valley", "Peak", "Colosseum", "Tidal", "Drowned"])
    st.text("")

    one1, one2, one3, one4, one5 = "Sandstone", "Red Sandstone", "Copper", "Coal", "Valley"
    two1, two2, two3, two4, two5 = "Lapis", "Amethyst", "Diamond", "Emerald", "Peak"
    three1, three2, three3, three4, three5 = "Iron", "Redstone", "Calcium", "Gold", "Colosseum"
    four1, four2, four3, four4, four5 = "Tube Coral", "Fire Coral", "Horn Coral", "Bubble Coral", "Tidal"
    five1, five2, five3, five4, five5 = "Seaweed", "Sea Floor", "Foreign Machinery", "Volcanic Rock", "Drowned"
with col2:
    st.subheader("Which block:")
    if realm == "Valley":
        mix = st.radio("", [f"{one1} - {one2} Mix", f"{one2} - {one3} Mix", f"{one3} - {one4} Mix", f"{one5} Mix"])
        
    if realm == "Peak":
        mix = st.radio("", [f"{two1} - {two2} Mix", f"{two2} - {two3} Mix", f"{two3} - {two4} Mix", f"{two5} Mix"])
        
    if realm == "Colosseum":
        mix = st.radio("", [f"{three1} - {three2} Mix", f"{three2} - {three3} Mix", f"{three3} - {three4} Mix", f"{three5} Mix"])
        
    if realm == "Tidal":
        mix = st.radio("", [f"{four1} - {four2} Mix", f"{four2} - {four3} Mix", f"{four3} - {four4} Mix", f"{four5} Mix"])
        
    if realm == "Drowned":
        mix = st.radio("", [f"{five1} - {five2} Mix", f"{five2} - {five3} Mix", f"{five3} - {five4} Mix", f"{five5} Mix"])

    
    
st.text("")
blocks = st.text_input("How many blocks:", value="0", max_chars=5, placeholder="0-99999, only numbers!")
blocks = float(blocks)

submixtoggle = st.toggle("Toggle sub-mixes for realm mixes")

if mix == f"{one1} - {one2} Mix":
    block1 = float(1) 
    block2 = float(1)
    block1n = f"{one1}"
    block2n = f"{one2}"
if mix == f"{one2} - {one3} Mix":
    block1 = float(4)
    block2 = float(4)
    block1n = f"{one2}"
    block2n = f"{one3}" 
if mix == f"{one3} - {one4} Mix": 
    block1 = float(8)
    block2 = float(8)
    block1n = f"{one3}"
    block2n = f"{one4}"    
if mix == f"{one5} Mix":
    mixblock1 = float(3*4)
    mixblockmid1 = float(3*4)
    mixblockmid2 = float(3*8)
    mixblock4 = float(3*8)
    mixblockpart1, mixblockpart2 = float(3), float(3)
    mixblock1n = f"{one2}"
    mixblock2n = f"{one3}"
    mixblock4n = f"{one4}"
    

if mix == f"{two1} - {two2} Mix":
    block1 = float(2)
    block2 = float(3)
    block1n = f"{two1}"
    block2n = f"{two2}"
if mix == f"{two2} - {two3} Mix":
    block1 = float(6)
    block2 = float(5)
    block1n = f"{two2}"
    block2n = f"{two3}"
if mix == f"{two3} - {two4} Mix":
    block1 = float(10)
    block2 = float(10)
    block1n = f"{two3}"
    block2n = f"{two4}"
if mix == f"{two5} Mix":
    mixblock1 = float(5*6)
    mixblockmid1 = float(5*5)
    mixblockmid2 = float(5*10)
    mixblock4 = float(5*10)
    mixblockpart1, mixblockpart2 = float(5), float(5)
    mixblock1n = f"{two2}"
    mixblock2n = f"{two3}"
    mixblock4n = f"{two4}"
    
    
if mix == f"{three1} - {three2} Mix":
    block1 = float(6)
    block2 = float(6)
    block1n = f"{three1}"
    block2n = f"{three2}"
if mix == f"{three2} - {three3} Mix":
    block1 = float(8)
    block2 = float(7)
    block1n = f"{three2}"
    block2n = f"{three3}"       
if mix == f"{three3} - {three4} Mix":
    block1 = float(13)
    block2 = float(13)
    block1n = f"{three3}"
    block2n = f"{three4}"        
if mix == f"{three5} Mix":
    mixblock1 = float(7*8)
    mixblockmid1 = float(7*7)
    mixblockmid2 = float(7*13)
    mixblock4 = float(7*13)
    mixblockpart1, mixblockpart2 = float(7), float(7)
    mixblock1n = f"{three2}"
    mixblock2n = f"{three3}"
    mixblock4n = f"{three4}"
    
            
if mix == f"{four1} - {four2} Mix":
    block1 = float(7)
    block2 = float(7)
    block1n = f"{four1}"
    block2n = f"{four2}"       
if mix == f"{four2} - {four3} Mix":
    block1 = float(10)
    block2 = float(8)
    block1n = f"{four2}"
    block2n = f"{four3}"       
if mix == f"{four3} - {four4} Mix":
    block1 = float(14)
    block2 = float(14)
    block1n = f"{four3}"
    block2n = f"{four4}"        
if mix == f"{four5} Mix":
    mixblock1 = float(7*10)
    mixblockmid1 = float(7*8)
    mixblockmid2 = float(7*14)
    mixblock4 = float(7*14)
    mixblockpart1, mixblockpart2 = float(7), float(7)
    mixblock1n = f"{four2}"
    mixblock2n = f"{four3}"
    mixblock4n = f"{four4}"
    
            
if mix == f"{five1} - {five2} Mix":
    block1 = float(9)
    block2 = float(9) 
    block1n = f"{five1}"
    block2n = f"{five2}"        
if mix == f"{five2} - {five3} Mix":
    block1 = float(11)
    block2 = float(11)
    block1n = f"{five2}"
    block2n = f"{five3}"        
if mix == f"{five3} - {five4} Mix":
    block1 = float(16)
    block2 = float(12)
    block1n = f"{five3}"
    block2n = f"{five4}"        
if mix == f"{five5} Mix":
    mixblock1 = float(10*11)
    mixblockmid1 = float(10*11)
    mixblockmid2 = float(10*16)
    mixblock4 = float(10*12)
    mixblockpart1, mixblockpart2 = float(10), float(10)
    mixblock1n = f"{five2}"
    mixblock2n = f"{five3}"
    mixblock4n = f"{five4}"
 
 
    
if mix == f"{one5} Mix":
    mixtotal1, mixtotalmid1, mixtotalmid2, mixtotal4 = round(mixblock1 * blocks), round(mixblockmid1 * blocks), round(mixblockmid2 * blocks), round(mixblock4 * blocks)
    mixtotalmid = mixtotalmid1+mixtotalmid2
    mixtotal1stack, mixtotalmidstack, mixtotal4stack = math.floor(mixtotal1/64), math.floor(mixtotalmid/64), math.floor(mixtotal4/64)
    mixtotal1stackleft, mixtotalmidstackleft, mixtotal4stackleft = mixtotal1-(mixtotal1stack*64), mixtotalmid-(mixtotalmidstack*64), mixtotal4-(mixtotal4stack*64)
    mixpart1, mixpart2 = round(mixblockpart1 * blocks), round(mixblockpart2 * blocks)
    mixpart1stack, mixpart2stack = math.floor(mixpart1/64), math.floor(mixpart2/64)
    mixpart1stackleft, mixpart2stackleft = mixpart1-(mixpart1stack*64), mixpart2-(mixpart2stack*64)
    if submixtoggle == True:
        st.header(f"You need {mixpart1} {mixblock1n} - {mixblock2n} Mix ({mixpart1stack} and {mixpart1stackleft} blocks)")
        st.header(f"You need {mixpart2} {mixblock2n} - {mixblock4n} Mix ({mixpart2stack} and {mixpart2stackleft} blocks)")
    else:
        st.header(f"You need {mixtotal1} T3 {mixblock1n} ({mixtotal1stack} stacks and {mixtotal1stackleft} blocks)")
        st.header(f"You need {mixtotalmid} T3 {mixblock2n} ({mixtotalmidstack} stacks and {mixtotalmidstackleft} blocks)")
        st.header(f"You need {mixtotal4} T3 {mixblock4n} ({mixtotal4stack} stacks and {mixtotal4stackleft} blocks)")
        pass
elif mix == f"{two5} Mix":
    mixtotal1, mixtotalmid1, mixtotalmid2, mixtotal4 = round(mixblock1 * blocks), round(mixblockmid1 * blocks), round(mixblockmid2 * blocks), round(mixblock4 * blocks)
    mixtotalmid = mixtotalmid1+mixtotalmid2
    mixtotal1stack, mixtotalmidstack, mixtotal4stack = math.floor(mixtotal1/64), math.floor(mixtotalmid/64), math.floor(mixtotal4/64)
    mixtotal1stackleft, mixtotalmidstackleft, mixtotal4stackleft = mixtotal1-(mixtotal1stack*64), mixtotalmid-(mixtotalmidstack*64), mixtotal4-(mixtotal4stack*64)
    mixpart1, mixpart2 = round(mixblockpart1 * blocks), round(mixblockpart2 * blocks)
    mixpart1stack, mixpart2stack = math.floor(mixpart1/64), math.floor(mixpart2/64)
    mixpart1stackleft, mixpart2stackleft = mixpart1-(mixpart1stack*64), mixpart2-(mixpart2stack*64)
    if submixtoggle == True:
        st.header(f"You need {mixpart1} {mixblock1n} - {mixblock2n} Mix ({mixpart1stack} and {mixpart1stackleft} blocks)")
        st.header(f"You need {mixpart2} {mixblock2n} - {mixblock4n} Mix ({mixpart2stack} and {mixpart2stackleft} blocks)")
    else:
        st.header(f"You need {mixtotal1} T3 {mixblock1n} ({mixtotal1stack} stacks and {mixtotal1stackleft} blocks)")
        st.header(f"You need {mixtotalmid} T3 {mixblock2n} ({mixtotalmidstack} stacks and {mixtotalmidstackleft} blocks)")
        st.header(f"You need {mixtotal4} T3 {mixblock4n} ({mixtotal4stack} stacks and {mixtotal4stackleft} blocks)")
        pass
elif mix == f"{three5} Mix":
    mixtotal1, mixtotalmid1, mixtotalmid2, mixtotal4 = round(mixblock1 * blocks), round(mixblockmid1 * blocks), round(mixblockmid2 * blocks), round(mixblock4 * blocks)
    mixtotalmid = mixtotalmid1+mixtotalmid2
    mixtotal1stack, mixtotalmidstack, mixtotal4stack = math.floor(mixtotal1/64), math.floor(mixtotalmid/64), math.floor(mixtotal4/64)
    mixtotal1stackleft, mixtotalmidstackleft, mixtotal4stackleft = mixtotal1-(mixtotal1stack*64), mixtotalmid-(mixtotalmidstack*64), mixtotal4-(mixtotal4stack*64)
    mixpart1, mixpart2 = round(mixblockpart1 * blocks), round(mixblockpart2 * blocks)
    mixpart1stack, mixpart2stack = math.floor(mixpart1/64), math.floor(mixpart2/64)
    mixpart1stackleft, mixpart2stackleft = mixpart1-(mixpart1stack*64), mixpart2-(mixpart2stack*64)
    if submixtoggle == True:
        st.header(f"You need {mixpart1} {mixblock1n} - {mixblock2n} Mix ({mixpart1stack} and {mixpart1stackleft} blocks)")
        st.header(f"You need {mixpart2} {mixblock2n} - {mixblock4n} Mix ({mixpart2stack} and {mixpart2stackleft} blocks)")
    else:
        st.header(f"You need {mixtotal1} T3 {mixblock1n} ({mixtotal1stack} stacks and {mixtotal1stackleft} blocks)")
        st.header(f"You need {mixtotalmid} T3 {mixblock2n} ({mixtotalmidstack} stacks and {mixtotalmidstackleft} blocks)")
        st.header(f"You need {mixtotal4} T3 {mixblock4n} ({mixtotal4stack} stacks and {mixtotal4stackleft} blocks)")
        pass
elif mix == f"{four5} Mix":
    mixtotal1, mixtotalmid1, mixtotalmid2, mixtotal4 = round(mixblock1 * blocks), round(mixblockmid1 * blocks), round(mixblockmid2 * blocks), round(mixblock4 * blocks)
    mixtotalmid = mixtotalmid1+mixtotalmid2
    mixtotal1stack, mixtotalmidstack, mixtotal4stack = math.floor(mixtotal1/64), math.floor(mixtotalmid/64), math.floor(mixtotal4/64)
    mixtotal1stackleft, mixtotalmidstackleft, mixtotal4stackleft = mixtotal1-(mixtotal1stack*64), mixtotalmid-(mixtotalmidstack*64), mixtotal4-(mixtotal4stack*64)
    mixpart1, mixpart2 = round(mixblockpart1 * blocks), round(mixblockpart2 * blocks)
    mixpart1stack, mixpart2stack = math.floor(mixpart1/64), math.floor(mixpart2/64)
    mixpart1stackleft, mixpart2stackleft = mixpart1-(mixpart1stack*64), mixpart2-(mixpart2stack*64)
    if submixtoggle == True:
        st.header(f"You need {mixpart1} {mixblock1n} - {mixblock2n} Mix ({mixpart1stack} and {mixpart1stackleft} blocks)")
        st.header(f"You need {mixpart2} {mixblock2n} - {mixblock4n} Mix ({mixpart2stack} and {mixpart2stackleft} blocks)")
    else:
        st.header(f"You need {mixtotal1} T3 {mixblock1n} ({mixtotal1stack} stacks and {mixtotal1stackleft} blocks)")
        st.header(f"You need {mixtotalmid} T3 {mixblock2n} ({mixtotalmidstack} stacks and {mixtotalmidstackleft} blocks)")
        st.header(f"You need {mixtotal4} T3 {mixblock4n} ({mixtotal4stack} stacks and {mixtotal4stackleft} blocks)")
elif mix == f"{five5} Mix":
    mixtotal1, mixtotalmid1, mixtotalmid2, mixtotal4 = round(mixblock1 * blocks), round(mixblockmid1 * blocks), round(mixblockmid2 * blocks), round(mixblock4 * blocks)
    mixtotalmid = mixtotalmid1+mixtotalmid2
    mixtotal1stack, mixtotalmidstack, mixtotal4stack = math.floor(mixtotal1/64), math.floor(mixtotalmid/64), math.floor(mixtotal4/64)
    mixtotal1stackleft, mixtotalmidstackleft, mixtotal4stackleft = mixtotal1-(mixtotal1stack*64), mixtotalmid-(mixtotalmidstack*64), mixtotal4-(mixtotal4stack*64)
    mixpart1, mixpart2 = round(mixblockpart1 * blocks), round(mixblockpart2 * blocks)
    mixpart1stack, mixpart2stack = math.floor(mixpart1/64), math.floor(mixpart2/64)
    mixpart1stackleft, mixpart2stackleft = mixpart1-(mixpart1stack*64), mixpart2-(mixpart2stack*64)
    if submixtoggle == True:
        st.header(f"You need {mixpart1} {mixblock1n} - {mixblock2n} Mix ({mixpart1stack} and {mixpart1stackleft} blocks)")
        st.header(f"You need {mixpart2} {mixblock2n} - {mixblock4n} Mix ({mixpart2stack} and {mixpart2stackleft} blocks)")
    else:
        st.header(f"You need {mixtotal1} T3 {mixblock1n} ({mixtotal1stack} stacks and {mixtotal1stackleft} blocks)")
        st.header(f"You need {mixtotalmid} T3 {mixblock2n} ({mixtotalmidstack} stacks and {mixtotalmidstackleft} blocks)")
        st.header(f"You need {mixtotal4} T3 {mixblock4n} ({mixtotal4stack} stacks and {mixtotal4stackleft} blocks)")
elif mix != f"{one5} Mix":  
    total1, total2 = round(block1 * blocks), round(block2 * blocks)
    total1stack, total2stack = math.floor(total1/64), math.floor(total2/64)
    total1stackleft, total2stackleft = total1-(total1stack*64), total2-(total2stack*64)
    st.header(f"You need {total1} T3 {block1n} ({total1stack} stacks and {total1stackleft} blocks)")
    st.header(f"You need {total2} T3 {block2n} ({total2stack} stacks and {total2stackleft} blocks)")
elif mix != f"{two5} Mix":  
    total1, total2 = round(block1 * blocks), round(block2 * blocks)
    total1stack, total2stack = math.floor(total1/64), math.floor(total2/64)
    total1stackleft, total2stackleft = total1-(total1stack*64), total2-(total2stack*64)
    st.header(f"You need {total1} T3 {block1n} ({total1stack} stacks and {total1stackleft} blocks)")
    st.header(f"You need {total2} T3 {block2n} ({total2stack} stacks and {total2stackleft} blocks)")
elif mix != f"{three5} Mix":  
    total1, total2 = round(block1 * blocks), round(block2 * blocks)
    total1stack, total2stack = math.floor(total1/64), math.floor(total2/64)
    total1stackleft, total2stackleft = total1-(total1stack*64), total2-(total2stack*64)
    st.header(f"You need {total1} T3 {block1n} ({total1stack} stacks and {total1stackleft} blocks)")
    st.header(f"You need {total2} T3 {block2n} ({total2stack} stacks and {total2stackleft} blocks)")
elif mix != f"{four5} Mix":  
    total1, total2 = round(block1 * blocks), round(block2 * blocks)
    total1stack, total2stack = math.floor(total1/64), math.floor(total2/64)
    total1stackleft, total2stackleft = total1-(total1stack*64), total2-(total2stack*64)
    st.header(f"You need {total1} T3 {block1n} ({total1stack} stacks and {total1stackleft} blocks)")
    st.header(f"You need {total2} T3 {block2n} ({total2stack} stacks and {total2stackleft} blocks)")
elif mix != f"{five5} Mix":  
    total1, total2 = round(block1 * blocks), round(block2 * blocks)
    total1stack, total2stack = math.floor(total1/64), math.floor(total2/64)
    total1stackleft, total2stackleft = total1-(total1stack*64), total2-(total2stack*64)
    st.header(f"You need {total1} T3 {block1n} ({total1stack} stacks and {total1stackleft} blocks)")
    st.header(f"You need {total2} T3 {block2n} ({total2stack} stacks and {total2stackleft} blocks)")
else:
    pass
