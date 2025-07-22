import instaloader
import os
import getpass
import time
from instaloader.structures import Post

def extrai_usuario(link_ou_user):
    if link_ou_user.startswith("http"):
        return link_ou_user.rstrip('/').split("/")[-1]
    elif link_ou_user.startswith("@"):
        return link_ou_user[1:]
    else:
        return link_ou_user

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

    # Login opcional
    fazer_login = input("Deseja fazer login(use uma conta fake)? (s/n): ").strip().lower()
    logado = False
    if fazer_login == 's':
        ig_user = input("Digite seu @ do Instagram: ")
        senha = getpass.getpass("Senha: ")
        try:
            loader.login(ig_user, senha)
            print("[✓] Login feito com sucesso!")
            logado = True
        except Exception as e:
            print(f"[X] Falha no login: {e}")
            return

    try:
        profile = instaloader.Profile.from_username(loader.context, usuario)

        # Salvar perfil.txt
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

        # Baixar foto perfil
        pasta_foto_perfil = os.path.join(base_path, "foto_perfil")
        os.makedirs(pasta_foto_perfil, exist_ok=True)
        loader.dirname_pattern = pasta_foto_perfil
        loader.download_profile(profile.username, profile_pic_only=True)

        # Baixar posts
        pasta_posts = os.path.join(base_path, "posts")
        os.makedirs(pasta_posts, exist_ok=True)
        loader.dirname_pattern = pasta_posts

        legendas_txt = os.path.join(base_path, "legendas.txt")
        comentarios_txt = os.path.join(base_path, "comentarios.txt")

        with open(legendas_txt, "w", encoding="utf-8") as l_file, \
             open(comentarios_txt, "w", encoding="utf-8") as c_file:

            posts = list(profile.get_posts())
            if not posts:
                print("[-] Nenhum post encontrado.")
            else:
                print(f"[→] Baixando {len(posts)} posts do feed...\n")
                for post in posts:
                    print(f"[+] Baixando post {post.date_utc.strftime('%Y-%m-%d')}")
                    loader.download_post(post, target=profile.username)
                    time.sleep(5)  # Delay para evitar bloqueio

                    # Legenda
                    l_file.write(f"DATA: {post.date_utc.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    l_file.write((post.caption or "[Sem legenda]") + "\n\n")

                    # Comentários
                    try:
                        for comment in post.get_comments():
                            c_file.write(f"{comment.owner.username} ({comment.created_at_utc}): {comment.text}\n")
                        c_file.write("\n---\n\n")
                    except Exception:
                        c_file.write("[Erro ao coletar comentários]\n\n")

        # Baixar reels
        pasta_reels = os.path.join(base_path, "reels")
        os.makedirs(pasta_reels, exist_ok=True)
        loader.dirname_pattern = pasta_reels

        reels = [post for post in profile.get_posts() if post.is_video and hasattr(post, 'is_reel') and post.is_reel]
        if not reels:
            print("[-] Nenhum Reel encontrado ou não acessível.")
        else:
            print(f"[→] Baixando {len(reels)} Reels...\n")
            for reel in reels:
                print(f"[+] Baixando Reel de {reel.date_utc.strftime('%Y-%m-%d')}")
                loader.download_post(reel, target=profile.username)
                time.sleep(5)  # Delay

        # Baixar stories (só se logado)
        if logado:
            print("[→] Baixando Stories...\n")
            try:
                stories = loader.get_stories(userids=[profile.userid])
                count_stories = 0
                for story in stories:
                    for item in story.get_items():
                        pasta_stories = os.path.join(base_path, "stories")
                        os.makedirs(pasta_stories, exist_ok=True)
                        loader.dirname_pattern = pasta_stories
                        loader.download_storyitem(item, target=profile.username)
                        count_stories += 1
                        time.sleep(3)  # Delay menor para stories
                if count_stories == 0:
                    print("[-] Nenhum story encontrado ou você não tem acesso.")
                else:
                    print(f"[+] {count_stories} stories baixados.")
            except Exception as e:
                print(f"[X] Erro ao baixar stories: {e}")
        else:
            print("[-] Não está logado, não será possível baixar stories.")

        # Salvar seguidores (só se logado)
        if logado:
            seguidores_txt = os.path.join(base_path, "seguidores.txt")
            seguidores = list(profile.get_followers())
            if not seguidores:
                print("[-] Nenhum seguidor encontrado ou não acessível.")
            else:
                print(f"[→] Salvando {len(seguidores)} seguidores...\n")
                with open(seguidores_txt, "w", encoding="utf-8") as f:
                    for follower in seguidores:
                        f.write(f"{follower.username}\n")
                print("[✓] Lista de seguidores salva.")
        else:
            print("[-] Não está logado, não será possível salvar seguidores.")

        print("\n[✓] Download completo!")

    except Exception as e:
        print(f"[X] Erro ao processar perfil: {e}")

if __name__ == "__main__":
    main()
