import instaloader
import os
import getpass
import time
import random
from instaloader.structures import Post

def extrai_usuario(link_ou_user):
    if link_ou_user.startswith("http"):
        return link_ou_user.rstrip('/').split("/")[-1]
    elif link_ou_user.startswith("@"):
        return link_ou_user[1:]
    else:
        return link_ou_user

def safe_get(func, *args, retries=5, delay=5):
    for i in range(retries):
        try:
            return func(*args)
        except Exception as e:
            print(f"[!] Tentativa {i+1} falhou: {e}")
            time.sleep(delay + i * random.randint(5, 10))
    return None

def main():
    nome_pasta = input("Digite o nome da pasta onde deseja salvar: ").strip()
    link_ou_user = input("Digite o link ou o @ da conta do Instagram: ").strip()
    usuario = extrai_usuario(link_ou_user)

    usuario_windows = os.getlogin()
    base_path = fr"C:/Users/{usuario_windows}/Documents/{nome_pasta}/{usuario}"
    os.makedirs(base_path, exist_ok=True)

    loader = instaloader.Instaloader(
        save_metadata=False,
        download_video_thumbnails=False,
        compress_json=False,
        download_comments=False,
        post_metadata_txt_pattern=""
    )
    
    # Login
    logado = False
    if input("Deseja fazer login(use uma conta fake)? (s/n): ").strip().lower() == 's':
        ig_user = input("Digite seu @ do Instagram: ")
        senha = getpass.getpass("Senha: ")
        try:
            loader.login(ig_user, senha)
            print("[✓] Login feito com sucesso!")
            logado = True
            time.sleep(10)  # Delay após login
        except Exception as e:
            print(f"[X] Falha no login: {e}")
            return

    try:
        profile = safe_get(instaloader.Profile.from_username, loader.context, usuario)
        if not profile:
            print("[X] Não foi possível acessar o perfil.")
            return

        # perfil.txt
        with open(os.path.join(base_path, "perfil.txt"), "w", encoding="utf-8") as f:
            f.write(f"Usuário: @{profile.username}\n")
            f.write(f"Nome: {profile.full_name}\n")
            f.write(f"Bio: {profile.biography}\n")
            f.write(f"Link externo: {profile.external_url}\n")
            f.write(f"Seguidores: {profile.followers}\n")
            f.write(f"Seguindo: {profile.followees}\n")
            f.write(f"Privado: {'Sim' if profile.is_private else 'Não'}\n")
            f.write(f"Verificado: {'Sim' if profile.is_verified else 'Não'}\n")
            f.write(f"Número de posts: {profile.mediacount}\n")

        # Foto perfil
        pasta_foto = os.path.join(base_path, "foto_perfil")
        os.makedirs(pasta_foto, exist_ok=True)
        loader.dirname_pattern = pasta_foto
        loader.download_profile(profile.username, profile_pic_only=True)

        # Posts
        pasta_posts = os.path.join(base_path, "posts")
        os.makedirs(pasta_posts, exist_ok=True)
        loader.dirname_pattern = pasta_posts

        l_txt = os.path.join(base_path, "legendas.txt")
        c_txt = os.path.join(base_path, "comentarios.txt")

        posts = safe_get(lambda: profile.get_posts())
        if not posts:
            print("[-] Nenhum post disponível ou acesso bloqueado.")
        else:
            print("[→] Baixando posts...\n")
            with open(l_txt, "w", encoding="utf-8") as l_file, open(c_txt, "w", encoding="utf-8") as c_file:
                for i, post in enumerate(posts):
                    print(f"[+] Post {i+1}: {post.date_utc.strftime('%Y-%m-%d')}")
                    loader.download_post(post, target=profile.username)
                    time.sleep(random.uniform(4, 8))

                    l_file.write(f"DATA: {post.date_utc}\n{post.caption or '[Sem legenda]'}\n\n")

                    try:
                        for c in post.get_comments():
                            c_file.write(f"{c.owner.username} ({c.created_at_utc}): {c.text}\n")
                        c_file.write("\n---\n\n")
                    except:
                        c_file.write("[Erro ao coletar comentários]\n\n")

        # Reels
        pasta_reels = os.path.join(base_path, "reels")
        os.makedirs(pasta_reels, exist_ok=True)
        loader.dirname_pattern = pasta_reels

        reels = [p for p in profile.get_posts() if p.is_video]
        if not reels:
            print("[-] Nenhum Reel disponível.")
        else:
            print(f"[→] Baixando {len(reels)} Reels...\n")
            for reel in reels:
                print(f"[+] Reel de {reel.date_utc.strftime('%Y-%m-%d')}")
                loader.download_post(reel, target=profile.username)
                time.sleep(random.uniform(4, 8))

        # Stories
        if logado:
            print("[→] Baixando Stories...\n")
            try:
                pasta_stories = os.path.join(base_path, "stories")
                os.makedirs(pasta_stories, exist_ok=True)
                loader.dirname_pattern = pasta_stories

                stories = loader.get_stories(userids=[profile.userid])
                count = 0
                for s in stories:
                    for item in s.get_items():
                        loader.download_storyitem(item, target=profile.username)
                        time.sleep(random.uniform(2, 5))
                        count += 1
                print(f"[✓] Stories baixados: {count}")
            except Exception as e:
                print(f"[X] Erro nos stories: {e}")
        else:
            print("[-] Login necessário para baixar stories.")

        # Seguidores
        if logado:
            print("[→] Salvando seguidores...\n")
            seguidores_txt = os.path.join(base_path, "seguidores.txt")
            try:
                seguidores = profile.get_followers()
                with open(seguidores_txt, "w", encoding="utf-8") as f:
                    for s in seguidores:
                        f.write(f"{s.username}\n")
                print("[✓] Seguidores salvos.")
            except Exception as e:
                print(f"[X] Erro ao salvar seguidores: {e}")
        else:
            print("[-] Login necessário para ver seguidores.")

        print("\n[✓] Download finalizado com sucesso!")

    except Exception as e:
        print(f"[X] Erro geral: {e}")

if __name__ == "__main__":
    main()
