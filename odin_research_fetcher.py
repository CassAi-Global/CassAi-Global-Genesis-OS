import urllib.request
import xml.etree.ElementTree as ET

class OdinCurriculumEngine:
    def __init__(self, search_query, max_results=5):
        self.search_query = search_query.replace(" ", "+")
        self.max_results = max_results
        self.api_url = f"http://export.arxiv.org/api/query?search_query=all:{self.search_query}&start=0&max_results={self.max_results}"

    def fetch_research(self):
        print(f"[\033[93mODIN\033[0m] Initiating Sovereign Data Pull: '{self.search_query.replace('+', ' ')}'")
        
        try:
            # Ping the academic vault
            response = urllib.request.urlopen(self.api_url)
            xml_data = response.read().decode('utf-8')
            root = ET.fromstring(xml_data)

            # Namespace for ArXiv XML
            ns = {'atom': 'http://www.w3.org/2005/Atom'}

            papers = []
            for entry in root.findall('atom:entry', ns):
                title = entry.find('atom:title', ns).text.strip()
                summary = entry.find('atom:summary', ns).text.strip()
                
                # Find the PDF link
                pdf_url = ""
                for link in entry.findall('atom:link', ns):
                    if link.attrib.get('title') == 'pdf':
                        pdf_url = link.attrib.get('href')

                papers.append({'title': title, 'summary': summary, 'pdf': pdf_url})

            self.format_for_notebook_lm(papers)

        except Exception as e:
            print(f"[\033[91mERROR\033[0m] Connection failed: {e}")

    def format_for_notebook_lm(self, papers):
        print("\n[\033[92mSUCCESS\033[0m] Research Downloaded. Ready for NotebookLM ingestion.\n")
        print("="*60)
        
        for idx, paper in enumerate(papers, 1):
            print(f"DOCUMENT {idx}: {paper['title']}")
            print(f"PDF LINK: {paper['pdf']}")
            print(f"ABSTRACT: {paper['summary'][:300]}...\n")
            print("-" * 60)

# --- EXECUTE THE ENGINE ---
# We are telling ODIN to pull research on Neurodiversity and Education
engine = OdinCurriculumEngine(search_query="Neurodiversity Education", max_results=3)
engine.fetch_research()
