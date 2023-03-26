import streamlit as st
import asyncio
from httpx_oauth.clients.google import GoogleOAuth2


async def write_authorization_url(client, redirect_uri):
    authorization_url = await client.get_authorization_url(
        redirect_uri,
        scope=["profile", "email"],
        extras_params={"access_type": "online"},
    )
    return authorization_url


async def write_access_token(client, redirect_uri, code):
    token = await client.get_access_token(code, redirect_uri)
    return token


async def get_user_info(client, token):
    user_id, user_email = await client.get_id_email(token)
    return user_id, user_email


async def revoke_token(client, token):
    return await client.revoke_token(token)

# <svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" class="bi bi-google" viewBox="0 0 16 16">
# <path d="M15.545 6.558a9.42 9.42 0 0 1 .139 1.626c0 2.434-.87 4.492-2.384 5.885h.002C11.978 15.292 10.158 16 8 16A8 8 0 1 1 8 0a7.689 7.689 0 0 1 5.352 2.082l-2.284 2.284A4.347 4.347 0 0 0 8 3.166c-2.087 0-3.86 1.408-4.492 3.304a4.792 4.792 0 0 0 0 3.063h.003c.635 1.893 2.405 3.301 4.492 3.301 1.078 0 2.004-.276 2.722-.764h-.003a3.702 3.702 0 0 0 1.599-2.431H8v-3.08h7.545z"/>
# </svg>

def login_button(authorization_url, app_name, app_desc):
    st.markdown('''<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="sameorigin">''',
    unsafe_allow_html=True)

    container = f'''
    <div class="col-md-12 text-center">
        <iframe src="static/login_popup.html#{authorization_url}" width="200" height="50" frameborder="0" scrolling="no" style="border:none;"></iframe>
    </div>
    '''

    st.markdown(container, unsafe_allow_html=True)


def login_button_temp2(authorization_url, app_name, app_desc):
    st.markdown('''<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="sameorigin">''',
    unsafe_allow_html=True)
    
    js = f"""
    <script>
        function openPopup() {{
            var w = 500;
            var h = 600;
            var left = (screen.width/2)-(w/2);
            var top = (screen.height/2)-(h/2);
            window.open("{authorization_url}", "Google Login", "width=" + w + ",height=" + h + ",top=" + top + ",left=" + left);
        }}
    </script>
    """

    container = f'''
    <div class="col-md-12 text-center">
        <button type="button" class="btn-lg btn-primary" onclick="openPopup()">
            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-google" viewBox="0 0 16 16">
            <path d="M15.545 6.558a9.42 9.42 0 0 1 .139 1.626c0 2.434-.87 4.492-2.384 5.885h.002C11.978 15.292 10.158 16 8 16A8 8 0 1 1 8 0a7.689 7.689 0 0 1 5.352 2.082l-2.284 2.284A4.347 4.347 0 0 0 8 3.166c-2.087 0-3.86 1.408-4.492 3.304a4.792 4.792 0 0 0 0 3.063h.003c.635 1.893 2.405 3.301 4.492 3.301 1.078 0 2.004-.276 2.722-.764h-.003a3.702 3.702 0 0 0 1.599-2.431H8v-3.08h7.545z"/>
            </svg>
            Logga in med Google
        </button>
    </div>
    '''

    st.markdown(js, unsafe_allow_html=True)
    st.markdown(container, unsafe_allow_html=True)


def login_button_temp(authorization_url, app_name, app_desc):
    st.markdown('''<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="sameorigin">''',
    unsafe_allow_html=True)
    container = f'''
    <div class="col-md-12 text-center">
        <a target="_target" href="{authorization_url}">
            <button type="button" class="btn-lg btn-primary">
            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="bi bi-google" viewBox="0 0 16 16">
            <path d="M15.545 6.558a9.42 9.42 0 0 1 .139 1.626c0 2.434-.87 4.492-2.384 5.885h.002C11.978 15.292 10.158 16 8 16A8 8 0 1 1 8 0a7.689 7.689 0 0 1 5.352 2.082l-2.284 2.284A4.347 4.347 0 0 0 8 3.166c-2.087 0-3.86 1.408-4.492 3.304a4.792 4.792 0 0 0 0 3.063h.003c.635 1.893 2.405 3.301 4.492 3.301 1.078 0 2.004-.276 2.722-.764h-.003a3.702 3.702 0 0 0 1.599-2.431H8v-3.08h7.545z"/>
            </svg>
            Logga in med Google</button>
        </a>
    </div>
    '''
    st.markdown(container, unsafe_allow_html=True)

    # img1 = "https://downloadr2.apkmirror.com/wp-content/uploads/2016/05/5735811c4301f.png"
    
    # st.markdown(
    #     f"""<a target="_self" style='display: block; text-align: center;' href={authorization_url}>
    #     <img src={img1} width="75" height="75"><button style='bottom: 0; border: 2px #4285F4; border-radius: 5px; background-color: white; color: #4285F4; font-size:18px; font-weight: 600; font-family:sans-serif; padding: 8px 8px;' type="button">Logga in med Google</button>
    #     </a>
    #     """,
    #     unsafe_allow_html=True,
    # )

def logout_button(button_text):
    if st.button(button_text):
        st.session_state["authentication_status"] = None
        # asyncio.run(
        #     revoke_token(
        #         client=st.session_state.client,
        #         token=st.session_state.token["access_token"],
        #     )
        # )
        st.session_state.user_email = None
        st.session_state.user_id = None
        st.session_state.token = None
        st.experimental_rerun()


def login(
    client_id,
    client_secret,
    redirect_uri,
    app_name="Logga in med Google",
    app_desc="",
    logout_button_text="Logga ut",
):
    st.session_state.client = GoogleOAuth2(client_id, client_secret)
    authorization_url = asyncio.run(
        write_authorization_url(
            client=st.session_state.client, redirect_uri=redirect_uri
        )
    )
    app_desc
    if "token" not in st.session_state:
        st.session_state.token = None

    if st.session_state.token is None:
        try:
            code = st.experimental_get_query_params()["code"]
        except:
            login_button(authorization_url, app_name, app_desc)
        else:
            # Verify token is correct:
            try:
                token = asyncio.run(
                    write_access_token(
                        client=st.session_state.client,
                        redirect_uri=redirect_uri,
                        code=code,
                    )
                )
            except:
                login_button(authorization_url, app_name, app_desc)
            else:
                # Check if token has expired:
                if token.is_expired():
                    login_button(authorization_url, app_name, app_desc)
                else:
                    st.session_state.token = token
                    st.session_state.user_id, st.session_state.user_email = asyncio.run(
                        get_user_info(
                            client=st.session_state.client, token=token["access_token"]
                        )
                    )
                    logout_button(button_text=logout_button_text)
                    return (st.session_state.user_id, st.session_state.user_email)
    else:
        logout_button(button_text=logout_button_text)
        return (st.session_state.user_id, st.session_state.user_email)
    


