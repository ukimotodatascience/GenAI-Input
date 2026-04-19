from urllib.parse import unquote


def cleanup_google_alert_url(url: str) -> str:
    """
    Googleアラートから取得する時用のURL整形
    Discord上でサムネイルが表示されないのを防ぐ
    """
    prefix = "https://www.google.com/url?rct=j&sa=t&url="
    if url.startswith(prefix):
        return unquote(url.replace(prefix, "", 1))
    return url