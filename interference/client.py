import requests
import sys

def main():
    if len(sys.argv) > 1:
        server_address = sys.argv[1]
    else:
        server_address = "llm_server:31337"
    
    print("=== Chat Interactivo con LLM ===")
    print("Escribe 'salir' o 'exit' para terminar")
    print("================================================")
    
    while True:
        try:
            prompt = input("\nTú > ").strip()
            
            if prompt.lower() in ["salir", "exit", "quit", "q"]:
                print("¡Hasta luego!")
                break
                            
            url = f"http://{server_address}/complete"
            data = {"prompt": prompt}
            
            resp = requests.post(url, json=data, timeout=30)
            if resp.status_code == 200:
                j = resp.json()
                print("\nModelo > " + j["snippet_executed"])
                if j["output"].strip():
                    print("\nSalida: " + j["output"].strip())
            else:
                print(f"\nError: {resp.status_code} {resp.text}")
                
        except KeyboardInterrupt:
            print("\n¡Hasta luego!")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()