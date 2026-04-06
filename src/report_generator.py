from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(df, ci_age, ci_interest, filename="report_mufti.pdf"):
    styles = getSampleStyleSheet()
    story = []

    def add(text):
        story.append(Paragraph(text, styles["Normal"]))
        story.append(Spacer(1,10))

    story.append(Paragraph("<b>Digital User Analysis Report</b>", styles["Title"]))
    story.append(Spacer(1,20))
    add("<b>Nama:</b> Mufti")
    add("<b>Step 1:</b> Data Generation & Feature Engineering")
    add("<b>Step 2:</b> Analysis & Confidence Interval")

    # Statistik
    add("<b>Statistical Summary</b>")
    add(f"Mean Umur: {ci_age['mean']:.2f}")
    add(f"CI Umur: ({ci_age['lower']:.2f}, {ci_age['upper']:.2f})")
    add(f"Mean Skor Minat Digital: {ci_interest['mean']:.2f}")
    add(f"CI Skor Minat Digital: ({ci_interest['lower']:.2f}, {ci_interest['upper']:.2f})")

    # Insight otomatis
    add("<b>Key Insights</b>")
    umur_mean = df['Umur'].mean()
    add(f"- Mayoritas pengguna berada di usia produktif ({umur_mean:.0f} tahun).")
    top_login = df['Kategori Waktu Login'].value_counts().idxmax()
    add(f"- Aktivitas login dominan terjadi pada {top_login}.")
    high_interest_pct = (df['Skor Minat Digital'] == 3).mean() * 100
    add(f"- {high_interest_pct:.0f}% pengguna memiliki minat digital tinggi → prioritas campaign.")
    top_loc = df['Tipe Lokasi'].value_counts().idxmax()
    add(f"- Tipe lokasi paling banyak: {top_loc}.")
    
    # Recommendation
    add("<b>Business Recommendations</b>")
    add("- Fokus campaign pada jam aktif dominan user.")
    add("- Target usia 25–40 sebagai core market.")
    add("- Prioritaskan high interest users.")
    add("- Promosi offline di lokasi paling ramai (Mall/Office).")
    add("- Gunakan email & WhatsApp sebagai channel utama.")
    add("- Edukasi digital untuk user low interest untuk meningkatkan engagement.")

    # Generate PDF
    doc = SimpleDocTemplate(filename)
    doc.build(story)
