import streamlit as st
import hydralit_components as hc
from annotated_text import annotated_text

#make it look nice from the start
st.set_page_config(layout='wide',page_icon="icon.png",page_title="نقاش علی اکبر",initial_sidebar_state='collapsed',)

# specify the primary menu definition




with open('c.css') as f:
    st.markdown(f'<style>{f.read()}</style>' ,unsafe_allow_html=True,)



st.markdown(" 🌈 نقاش علی اکبر - بندرعباس 🌈" )


menu_data = [

    
    {'id':'صفحه اصلی','icon': "🏠", 'label':"صفحه اصلی",},
    {'id':'تماس با من','icon':"☎️",'label':"تماس با من"},
    {'id':'','icon': "🎨",'label':"نمونه کارها", },
    {'id':'خدمات نقاش','icon': "📙", 'label':"خدمات نقاش"},
    
]

over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    
    
#     home_name='Home',
#     login_name='Logout',
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned

)



#get the id of the menu item clicked
st.info(f"{menu_id}")


if menu_id == 'صفحه اصلی':
    
    st.snow()

    col1,col2 = st.columns(2)

    with col1:
        annotated_text(
    "خدمات ",
    ("انواع", "نقاشی ساختمان"),
    " رنگ پلاستیک ",
    ("و", "اکرولیک"),
    " روغنی ",
    ("کناف", "رنگ آمیزی"),
    "درب و پنجره",
    ("با بهترین کیفیت", "در"),
    "  ",
    ("خدمت", "مشتریهای"),
    " عزیز ",
    "."
)
        st.caption("نقاشی ساختمان سر تا سر بندرعباس پذیرفته میشه")
    with col2:
        st.image("https://azinpeyman.com/wp-content/uploads/2021/09/%D8%B1%D9%88%D8%B4-%D9%87%D8%A7%DB%8C-%D8%B1%D9%86%DA%AF-%D8%A2%D9%85%DB%8C%D8%B2%DB%8C-%D8%AF%DB%8C%D9%88%D8%A7%D8%B1-%D9%88-%D8%A7%D8%AA%D8%A7%D9%82.jpg")


if menu_id == 'تماس با من':
    
    st.markdown("علی اکبر بندرعباس : ☎️ 09337382190")
    

   



if menu_id == 'نمونه کارها':
    
    col1,col2,col3=st.columns((3))
    with col1:
        with st.expander(expanded=True,label="کد 10"):
            st.image('https://naqashaliakbar.vercel.app/a1.jpg')
            st.caption("رنگ سفید و طلایی جای کولر")
            st.markdown("[باز کردن نمونه کار](https://naqashaliakbar.vercel.app/a1.jpg)")

    with col2:
        with st.expander(expanded=True,label="کد 20"):
            st.image('https://naqashaliakbar.vercel.app/a2.jpg')
            st.caption("رنگ آمیزی کمد دیواری ")
            st.markdown("[باز کردن نمونه کار](https://naqashaliakbar.vercel.app/a2.jpg)")


    with col3:
        with st.expander(expanded=True,label="کد 30"):
            st.image('https://naqashaliakbar.vercel.app/a3.jpg')
            st.caption("رنگ آمیزی درب ")
            st.markdown("[باز کردن نمونه کار](https://naqashaliakbar.vercel.app/a3.jpg)")










    with col1:
        with st.expander(expanded=True,label="کد 40"):
            st.image('https://naqashaliakbar.vercel.app/a4.jpg')
            st.caption("رنگ آمیزی درب سفید و طلایی ")
            st.markdown("[باز کردن نمونه کار](https://naqashaliakbar.vercel.app/a4.jpg)")

    with col2:
        with st.expander(expanded=True,label="کد 50"):
            st.image('https://naqashaliakbar.vercel.app/a5.jpg')
            st.caption("رنگ آمیزی درب ")
            st.markdown("[باز کردن نمونه کار](https://naqashaliakbar.vercel.app/a5.jpg)")


    with col3:
        with st.expander(expanded=True,label="کد 60"):
            st.image('https://naqashaliakbar.vercel.app/a6.jpg')
            st.caption("رنگ آمیزی استخر ")
            st.markdown("[باز کردن نمونه کار](https://naqashaliakbar.vercel.app/a6.jpg)")








    with col1:
        with st.expander(expanded=True,label="کد 70"):
            st.image('https://naqashaliakbar.vercel.app/a7.jpg')
            st.caption("رنگ آمیزی کناف ")
            st.markdown("[باز کردن نمونه کار](https://naqashaliakbar.vercel.app/a7.jpg)")

    with col2:
        with st.expander(expanded=True,label="کد 80"):
            st.image('https://naqashaliakbar.vercel.app/a8.jpg')
            st.caption("رنگ دیوار با طرح برگ ")
            st.markdown("[باز کردن نمونه کار](https://naqashaliakbar.vercel.app/a8.jpg)")


    with col3:
        with st.expander(expanded=True,label="کد 90"):
            st.image('https://naqashaliakbar.vercel.app/a9.jpg')
            st.caption("رنگ دیوار با طرح برگ ")
            st.markdown("[باز کردن نمونه کار](https://naqashaliakbar.vercel.app/a9.jpg)")






    with col1:
        with st.expander(expanded=True,label="کد 100"):
            st.image('https://naqashaliakbar.vercel.app/a10.jpg')
            st.caption("رنگ دیوار ساده ")
            st.markdown("[باز کردن نمونه کار](https://naqashaliakbar.vercel.app/a10.jpg)")

    with col2:
        with st.expander(expanded=True,label="کد 110"):
            st.image('https://naqashaliakbar.vercel.app/a11.jpg')
            st.caption("رنگ آمیزی کناف ")
            st.markdown("[باز کردن نمونه کار](https://naqashaliakbar.vercel.app/a11.jpg)")


   













if menu_id == 'خدمات نقاش':
    st.markdown("""
    خدمات نقاشی ساختمان چیست؟

نقاشی ساختمان همان زیر سازی و ترمیم و رنگ آمیزی با رنگهای ساختمانی است که شامل دو بخش داخل ساختمان و خارج ساختمان (رنگ نما) می شود . در واقع قدمتی 150 ساله دارد و برای تمیزی و زندگی سالم شهری امروزه یکی از ملزومات واجبی است که باید انجام شود .در ادامه به معرفی انواع رنگ ساختمان، انواع ابزار نقاشی ساختمان و در انتها انواع خدمات نقاشی ساختمان می‌پردازیم.
انواع رنگ ساختمان

رنگهای ساختمانی دارای ساختار شیمیایی متفاوتی هستند که آنها را از هم متمایز می کند .انواع رنگ شامل رنگ پلاستیک، اکریلیک، روغن، مولتی کالر، بلکا، متالیک، اپوکسی و …است؛پرکاربردترین رنگ‌ها در خدمات نقاشی ساختمان مخصوصاً منازل رنگ پلاستیک، رنگ اکریلیک و رنگ روغن است.
    """)
    


    



st.divider()


st.markdown("[طراحی شده توسط عبدالله چلاسی](https://abdollahchelasi.ir)")


st.markdown("""
<style> 
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)