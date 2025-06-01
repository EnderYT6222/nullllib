import os

class Pytools:
    def __init__(self, base_folder="void_scripts"):
        self.base_folder = base_folder
        if not os.path.exists(base_folder):
            os.makedirs(base_folder)

    def list_v0id_files(self):
        """Base klasöründeki .v0id dosyalarını listeler."""
        files = []
        for f in os.listdir(self.base_folder):
            if f.endswith(".v0id"):
                files.append(f)
        return files

    def run_v0id(self, filename):
        """Verilen .v0id dosyasını çalıştırır."""
        path = os.path.join(self.base_folder, filename)
        if not os.path.isfile(path):
            return f"⚠️ Dosya bulunamadı: {filename}"

        try:
            with open(path, "r", encoding="utf-8") as f:
                code = f.read()
            # Python kodu gibi çalıştırıyoruz
            exec_globals = {}
            exec(code, exec_globals)
            return "✅ Çalıştırma başarılı."
        except Exception as e:
            return f"❌ Hata oluştu: {e}"
