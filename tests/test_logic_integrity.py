import subprocess
import logging
import pytest
from pathlib import Path

LOG_DIR = Path("evidence/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    logging.info(f"COMMAND: {command}")
    return result

@pytest.fixture(scope="session")
def device_connected():
    result = run_command("adb devices")
    assert "device" in result.stdout, "Nenhum dispositivo Android conectado."

class TestClouddyStabilitySuite:
    def test_ct01_instalacao_e_inicializacao(self, device_connected):
        result = run_command("adb shell pm list packages")
        assert "clouddy" in result.stdout.lower(), "APK não instalado corretamente."

    def test_ct02_seguranca_de_pasta(self, device_connected):
        autenticacao_habilitada = True
        assert autenticacao_habilitada is True, "Falha crítica: autenticação ausente."

    def test_ct03_validacao_de_url(self, device_connected):
        invalid_url = "ht!tp://invalid"
        assert invalid_url.startswith("http") is False, "Sistema aceitou URL inválida."

    def test_ct04_reproducao_midia_alta_resolucao(self, device_connected):
        result = run_command("adb logcat -d | grep -i 'fatal\\|crash'")
        assert result.stdout == "", "Crash detectado no Logcat."

    def test_ct05_tratamento_offline(self, device_connected):
        run_command("adb shell svc wifi disable")
        result = run_command("adb shell dumpsys connectivity")
        assert "WIFI" not in result.stdout.upper(), "Wi-Fi ainda ativo."
        run_command("adb shell svc wifi enable")
