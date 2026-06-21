Installation/Konfiguration:
 - optional: MS Terminal und MS PowerShell installieren
 - WSL installieren
    -> wsl --install
        -> Test auf WSl2 -> wsl -l -v
 - WSL Distribution installieren
    -> wsl --list --online
        -> wsl --install Ubuntu-26.04

 - Docker Desktop installieren
    -> https://www.docker.com/
        -> Windows 11 AMD 64
    -> "Use WSL 2 instead of Hyper-V"
    -> reboot Windows und Start Docker
    -> optional: Docker Account erstellen
    -> in Docker Desktop: Settings -> Ressources -> WSL integration -> Distro aktivieren

 - VS Code installieren
    -> https://code.visualstudio.com/Download
    -> VS Code innerhalb WSL betreiben (unten links) (ToDo: noch zu beschreiben)
    -> Extension "Dev Containers" installieren
     
 - Github Repository:
    -> Repository: ConTcoN / agent-sandbox
    -> lokales Repository in WSL in eigenen User Bereich clonen
 
 - VS Code starten und Popup folgen (Rebuild Container)
    -> unten links "Dev Container: Agent Sandbox"
