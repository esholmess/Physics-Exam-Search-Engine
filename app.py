import streamlit as st
import google.generativeai as genai
from physics_data import ELECTROMAGNETISM_DB

# Set page configuration
st.set_page_config(
    page_title="Physics Search Engine",
    page_icon="🔬",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    body, .main {
        background-color: #181818 !important;
        color: #f6e27a !important;
    }
    .custom-header {
        background: linear-gradient(90deg, #232526 0%, #414345 100%);
        color: #f6e27a;
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 24px rgba(0,0,0,0.25);
        text-align: center;
    }
    .custom-header h1 {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.2em;
        letter-spacing: 1px;
        color: #f6e27a;
        text-shadow: 0 2px 8px #23252655;
    }
    .custom-header h3 {
        font-size: 1.2rem;
        font-weight: 400;
        color: #e0e0e0;
        margin-bottom: 0;
    }
    .stTextInput>div>div>input {
        background: #232526 !important;
        color: #f6e27a !important;
        border: 1.5px solid #f6e27a !important;
        border-radius: 8px !important;
        font-size: 1.15rem !important;
        padding: 0.7rem 1rem !important;
        box-shadow: 0 2px 8px #23252633;
    }
    .stTextInput>div>div>input:focus {
        border: 2px solid #f6e27a !important;
        outline: none !important;
        background: #232526 !important;
    }
    .card {
        background: #232526 !important;
        border: 1.5px solid #f6e27a !important;
        color: #f6e27a !important;
        box-shadow: 0 2px 12px #23252655;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    .equation {
        background: #181818 !important;
        color: #f6e27a !important;
        border: 1px solid #f6e27a33 !important;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        text-align: center;
    }
    .warning-box {
        background: #ff6b6b !important;
        color: #fff !important;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        text-align: center;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    .stMarkdown, .stMarkdown p {
        color: #f6e27a !important;
    }
    @media (max-width: 768px) {
        .card {
            padding: 1rem;
        }
        .custom-header h1 {
            font-size: 2rem;
        }
        .custom-header h3 {
            font-size: 1rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="custom-header">
        <h1>🔬 Physics Search Engine</h1>
        <h3>Elektrik ve Manyetizma konularını keşfedin</h3>
    </div>
""", unsafe_allow_html=True)

# Gemini API yapılandırması
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)


def is_physics_topic(query: str) -> bool:
    """Girilen konunun fizik konusu olup olmadığını kontrol et"""
    physics_keywords = [
        'elektrik', 'manyetizma', 'kuvvet', 'alan', 'potansiyel', 'enerji',
        'sığa', 'kondansatör', 'indüksiyon', 'akım', 'voltaj', 'direnç',
        'ohm', 'coulomb', 'gauss', 'faraday', 'maxwell', 'amper', 'manyetik',
        'elektriksel', 'kapasitans', 'indüktans', 'empedans', 'reaktans'
    ]
    return any(keyword in query.lower() for keyword in physics_keywords)

def get_gemini_explanation(query: str) -> str:
    """Gemini API kullanarak fizik konuları hakkında açıklama al"""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(
            f"""Lütfen aşağıdaki elektrik ve manyetizma konusu hakkında detaylı bilgi ver:
            Konu: {query}
            
            Lütfen şu başlıklar altında bilgi ver:
            1. Temel Açıklama
            2. Örnekler
            3. Günlük Hayattan Uygulamalar
            
            Bilgileri Türkçe olarak, anlaşılır bir dille açıkla.
            Eğer konu elektrik ve manyetizma ile ilgili değilse, bunu belirt ve elektrik-manyetizma konularına yönlendir."""
        )
        return response.text
    except Exception as e:
        return f"AI açıklaması alınamadı: {str(e)}"

def search_physics(query: str):
    """Veritabanında arama yap"""
    results = []
    query = query.lower()
    
    for key, value in ELECTROMAGNETISM_DB.items():
        if (query in key or 
            query in value["title"].lower() or 
            query in value["content"].lower()):
            results.append(value)
    
    return results

def display_equation(equation: str):
    """Display a LaTeX equation in a formatted box"""
    st.markdown(f"""
    <div class="equation">
        ${equation}$
    </div>
    """, unsafe_allow_html=True)

def main():
    # Arama çubuğu
    query = st.text_input("Fizik kavramını arayın:", placeholder="örn: elektrik alan, manyetik akı, indüksiyon")
    
    if query:
        if not is_physics_topic(query):
            st.markdown("""
                <div class="warning-box">
                    ⚠️ Bu konu elektrik ve manyetizma ile ilgili görünmüyor. 
                    Lütfen elektrik ve manyetizma konuları hakkında arama yapın.
                    Örnek konular: elektrik alanı, manyetik akı, indüksiyon, sığa, kondansatör
                </div>
            """, unsafe_allow_html=True)
            return

        # Veritabanından sonuçları al
        db_results = search_physics(query)
        
        # AI açıklamasını al
        ai_explanation = get_gemini_explanation(query)
        
        # Sonuçları göster
        if db_results:
            st.subheader("📚 Veritabanı Sonuçları")
            for result in db_results:
                st.markdown(f"""
                    <div class="card">
                        <h3>{result['title']}</h3>
                        <p>{result['content']}</p>
                        <h4>Temel Denklemler:</h4>
                """, unsafe_allow_html=True)
                
                for eq in result["equations"]:
                    display_equation(eq)
                
                st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="card">
                    <p>Veritabanında bu konu ile ilgili sonuç bulunamadı. 
                    Ancak AI açıklaması aşağıda verilmiştir.</p>
                </div>
            """, unsafe_allow_html=True)
        
        # AI açıklamasını göster
        st.markdown("""
            <div class="card">
                <h3>🤖 AI Açıklaması</h3>
        """, unsafe_allow_html=True)
        st.write(ai_explanation)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()