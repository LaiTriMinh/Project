import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image



smoothies_model = pickle.load(open(r'C:\Users\Admin\Desktop\project aI\smoothies_model.sav', 'rb'))



with st.sidebar:
    
    selected = option_menu('Choose smoothie base on age and emotion',
                          
                          ['Smoothie Suggestions',
                          'Smoothies list'],
                          icons=['food','list'],
                          default_index=0)
    
    

if (selected == 'Smoothie Suggestions'):
    

    st.title('Smoothies base on emotion')
    
    
 
    col1, col2, col3 = st.columns(3)
    
    with col1:
        GENDER = st.text_input('Gender "1: Male, 0: Female"')
        
    with col2:
        AGE = st.text_input('Age "1-80"')
    
    with col3:
        EMOTION = st.text_input('How do you feel today?  "0: sadness, 1: joy, 2: fear, 3: anger, 4: love, 5: surprise, 6: worry, 7: enthusiasm, 8: empty, 9: happiness, 10: fun, 11: neutral" ')
    
    with col1:
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\age.jpg")
        st.image(image, caption='Welcome', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

    with col2:
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\smoothie life.jpg")
        st.image(image, caption='Smoothie life', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

    with col3:
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\feel.jpg")
        st.image(image, caption='How do you feel', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


    pre_smoothies = ''
    

    
    if st.button('Smoothies Result'):
        smoothies_prediction = smoothies_model.predict([[EMOTION, AGE, GENDER]])
        
        if (smoothies_prediction[0] == 10):
            pre_smoothies='Whats wrong an Orange Smoothies will help you out'
        elif (smoothies_prediction[0] == 12):
            pre_smoothies='Scare me, Waa, I will give you a Pineapple Green Smoothies and we are friend'
        elif (smoothies_prediction[0] == 13):
            pre_smoothies='A Strawberry Cheesecake Smoothies will help you calm'
        elif (smoothies_prediction[0] == 15):
            pre_smoothies='Get a Chocolate Peanut Butter Banana Smoothies, and tell me your story'
        elif (smoothies_prediction[0] == 16):
            pre_smoothies='A Oceanside Smoothies will make you forget about that'
        elif (smoothies_prediction[0] == 18):
            pre_smoothies='A Low- Sugar Blueberry Smoothies '
        elif (smoothies_prediction[0] == 111):
            pre_smoothies='Whats wrong an Orange Smoothie will help you out'
        elif (smoothies_prediction[0] == 20):
            pre_smoothies='The word ‘happiness’ may lose its meaning if it were not balanced by ‘sadness’. Wanna Kale Banana Smoothies?'
        elif (smoothies_prediction[0] == 22):
            pre_smoothies='Whats happen? Wanna Spinach Apple Smoothies'
        elif (smoothies_prediction[0] == 23):
            pre_smoothies='"Smile, even if it’s a sad smile, because sadder than a sad smile is the sadness of not knowing how to smile". By "Mr.Honeydew Melon Cucumber Smoothies"'
        elif (smoothies_prediction[0] == 25):
            pre_smoothies='Get a Spinach And Kale Smoothie, and tell me your story'
        elif (smoothies_prediction[0] == 26):
            pre_smoothies='Papaya Smoothie'
        elif (smoothies_prediction[0] == 28):
            pre_smoothies='"Sometimes, life will kick you around, but sooner or later, you realize you’re not just a survivor. You’re a warrior, and you’re stronger than anything life throws your way", by "Mr.Banana Smoothiess"'
        elif (smoothies_prediction[0] == 211):
            pre_smoothies='Im here with you, dont be neutral'
        elif (smoothies_prediction[0] == 30):
            pre_smoothies='Whats wrong an Avocado smoothie will help you out. It will help you slow aging'
        elif (smoothies_prediction[0] == 32):
            pre_smoothies='Tell me what make you scare, an Strawberry smoothie mix with Orange will help you out'
        elif (smoothies_prediction[0] == 33):
            pre_smoothies='Long-term anger will give you those wrinkles, why dont you try a strawberry mix cucumber smoothies'
        elif (smoothies_prediction[0] == 35):
            pre_smoothies='Boom, surprise again lol. lets try an papaya smoothie to make your day ?'
        elif (smoothies_prediction[0] == 36):
            pre_smoothies='Every things is gonna be allright. Banana smoothie will also be a great choice to relieve stress'
        elif (smoothies_prediction[0] == 38):
            pre_smoothies='Lear to be alone, thats the great things. An Yogurt and walnut smoothies is gonna warm your heart'
        elif (smoothies_prediction[0] == 311):
            pre_smoothies='Normal things Huh!. Wanna Apple smoothies?'
        elif (smoothies_prediction[0] == 0):
            pre_smoothies='Dont lie baby dont know sad, Watermelon smoothies is rich in vitamins A, C, calcium and carotene, good for babys vision'
        elif (smoothies_prediction[0] == 2):
            pre_smoothies='Superman here baby dont be scare; a banana, 1/4 cheese/yogurt, 1/4 cup orange juice will make the best smoothies'
        elif (smoothies_prediction[0] == 3):
            pre_smoothies='Mango smoothies, the BEST'
        elif (smoothies_prediction[0] == 5):
            pre_smoothies='How about Banana, avocado, and yogurt smoothie and mix it up'
        elif (smoothies_prediction[0] == 6):
            pre_smoothies='Whats wrong an Orange Smoothie will help you out'
        elif (smoothies_prediction[0] == 8):
            pre_smoothies='Lets by two Orange Smoothie and find a friend'
        elif (smoothies_prediction[0] == 11):
            pre_smoothies='Huh, fun story wanna Coconut Pie Smoothie'
        elif (smoothies_prediction[0] == 14):
            pre_smoothies='Love aghh I want it too, Lets try Love Smoothies, which contains avocado, mango, spinach, broccoli, coconut, ginger and lime. '
        elif (smoothies_prediction[0] == 17):
            pre_smoothies='Have a Banana Smoothies, and keep that spirit'
        elif (smoothies_prediction[0] == 19):
            pre_smoothies='I am glad to here that, make your day with a Blueberry Smoothies'
        elif (smoothies_prediction[0] == 110):
            pre_smoothies='TROPICAL PINEAPPLE SMOOTHIE will give you much energy to laugh more'
        elif (smoothies_prediction[0] == 21):
            pre_smoothies='Bravo, wanna Coconut Smoothies'
        elif (smoothies_prediction[0] == 24):
            pre_smoothies='Beautiful age to love, get a Peaches Smoothies and tell me about your partner'
        elif (smoothies_prediction[0] == 27):
            pre_smoothies='How about a Raspberry Smoothies, its my favorite'
        elif (smoothies_prediction[0] == 29):
            pre_smoothies='Happy is the best word I have heard today, a Grape Smoothie make you more'
        elif (smoothies_prediction[0] == 210):
            pre_smoothies='Huh, fun story wanna Coconut Pie Smoothie'
        elif (smoothies_prediction[0] == 31):
            pre_smoothies='Glad to hear that, how about a Chocolate Strawberries Smoothies'
        elif (smoothies_prediction[0] == 34):
            pre_smoothies='Love has no age, a Cinnamon Apple Smoothies will make your day'
        elif (smoothies_prediction[0] == 37):
            pre_smoothies='Keep that enthusiasm with a Watermelon Smoothie'
        elif (smoothies_prediction[0] == 39):
            pre_smoothies='I am happy too, Kiwi Smoothies is that OK'
        elif (smoothies_prediction[0] == 310):
            pre_smoothies='Cherry smoothies slow aging  '
        elif (smoothies_prediction[0] == 1):
            pre_smoothies='Peach smoothies and fresh milk help children get rid of constipation'
        elif (smoothies_prediction[0] == 4):
            pre_smoothies='Pineapple, celery and yogurt smoothies help children get rid of constipation'
        elif (smoothies_prediction[0] == 7):
            pre_smoothies='Melon smoothies help children get rid of constipation'
        elif (smoothies_prediction[0] == 9):
            pre_smoothies='Carrot and apple smoothies help children get rid of constipation'
        elif (smoothies_prediction[0] == 10):
            pre_smoothies='Carrot and apple smoothies help children get rid of constipation'


        else:
            pre_smoothies='lets see, How about Orange Smoothies good for all age'
        
    st.success(pre_smoothies)

if (selected == 'Smoothies list'):
    st.title('Our smoothies list')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Acai Berry Smoothie Bowl.jpeg")
        st.image(image, caption='Acai Berry Smoothie Bowl', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Banana and Walnut Smoothie.jpeg")
        st.image(image, caption='Banana and Walnut Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Berry-licious Smoothie Bowl.jpeg")
        st.image(image, caption='Berry-licious Smoothie Bowl', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Blueberry and Chia Seed Smoothie.jpeg")
        st.image(image, caption='Blueberry and Chia Seed Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Blueberry Blast Smoothie.jpeg")
        st.image(image, caption='Blueberry Blast Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Blueberry-Almond Smoothie.jpeg")
        st.image(image, caption='Blueberry-Almond Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open("C:/Users/Admin/Desktop/project aI/Carrot-Pineapple Smoothie.jpeg")
        st.image(image, caption='Carrot-Pineapple Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Cherry-Almond Smoothie.jpeg")
        st.image(image, caption='Cherry-Almond Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Coconut Water Smoothie with Mango, Banana and Strawberries.jpeg")
        st.image(image, caption='Coconut Water Smoothie with Mango, Banana and Strawberries', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Cran-Sicle Smoothie.jpeg")
        st.image(image, caption='Cran-Sicle Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Green Morning Smoothie.jpeg")
        st.image(image, caption='Green Morning Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Green Smoothie Bowl.jpeg")
        st.image(image, caption='Green Smoothie Bowl', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Green Smoothie.jpeg")
        st.image(image, caption='Green Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Healthy Breakfast Smoothie.jpeg")
        st.image(image, caption='Healthy Breakfast Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

    with col2:
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Healthy Cherry Almond Oatmeal Smoothie.jpeg")
        st.image(image, caption='Healthy Cherry Almond Oatmeal Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Keto Mint Chip Breakfast Smoothie.jpeg")
        st.image(image, caption='Keto Mint Chip Breakfast Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Kiwi-Ginger Zinger Protein Smoothie.jpeg")
        st.image(image, caption='Kiwi-Ginger Zinger Protein Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Mango, Strawberry, and Pineapple Smoothie.jpeg")
        st.image(image, caption='Mango, Strawberry, and Pineapple Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Matcha-Do About Nuttin'.jpeg")
        st.image(image, caption='Matcha Do About Nuttin', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Mean Green Smoothie.jpeg")
        st.image(image, caption='Mean Green Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Mixed Berries and Banana Smoothie (and Smoothie Bowl).jpeg")
        st.image(image, caption='Mixed Berries and Banana Smoothie (and Smoothie Bowl)', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Mixed Berries and Banana Smoothie.jpeg")
        st.image(image, caption='Mixed Berries and Banana Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Oatmeal Cookie Smoothie.jpeg")
        st.image(image, caption='Oatmeal Cookie Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Orange Banana Smoothie.jpeg")
        st.image(image, caption='Orange Banana Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Papaya-Banana Smoothie.jpeg")
        st.image(image, caption='Papaya-Banana Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Passion Fruit-Mango Smoothie.jpeg")
        st.image(image, caption='Passion Fruit-Mango Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Peach Pie Smoothie.jpeg")
        st.image(image, caption='Peach Pie Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Peachy Oat Smoothie.jpeg")
        st.image(image, caption='Peachy Oat Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")



    with col3:
        st.write(' ')

        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Peanut Butter Smoothie Bowl.jpeg")
        st.image(image, caption='Peanut Butter Smoothie Bowl', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Peanut Butter Split Smoothie.jpeg")
        st.image(image, caption='Peanut Butter Split Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Pineapple Smoothie Bowl.jpeg")
        st.image(image, caption='Pineapple Smoothie Bowl', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Pumpkin-Ginger Smoothie.jpeg")
        st.image(image, caption='Pumpkin-Ginger Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Raspberry-Vanilla Smoothie.jpeg")
        st.image(image, caption='Raspberry-Vanilla Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Red Berry-and-Beet Smoothie.jpeg")
        st.image(image, caption='Red Berry-and-Beet Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Strawberry-Banana Smoothie.jpeg")
        st.image(image, caption='Strawberry-Banana Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Strawberry-Green Tea Smoothie.jpeg")
        st.image(image, caption='Strawberry-Green Tea Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Super Green Smoothie.jpeg")
        st.image(image, caption='Super Green Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Tropical Oatmeal Smoothie.jpeg")
        st.image(image, caption='Tropical Oatmeal Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Ultra-Creamy Avocado Smoothie.jpeg")
        st.image(image, caption='Ultra-Creamy Avocado Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Vanilla Bean Coconut Yogurt Smoothie.jpeg")
        st.image(image, caption='Vanilla Bean Coconut Yogurt Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Vietnamese Coffee Smoothie.jpeg")
        st.image(image, caption='Vietnamese Coffee Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
        image = Image.open(r"C:\Users\Admin\Desktop\project aI\Watermelon-and-Cucumber Smoothie.jpeg")
        st.image(image, caption='Watermelon-and-Cucumber Smoothie', width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")




