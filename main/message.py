def message(user, random_number):
    return f"""<!-- templates/email/verification.html -->
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MiniWiki — Tasdiqlash kodi</title>
  </head>
  <body style="margin:0;padding:0;background:#f4f6fb;font-family:Arial, Helvetica, sans-serif;">
    <table width="100%" cellpadding="0" cellspacing="0" role="presentation">
      <tr>
        <td align="center" style="padding:30px 10px;">
          <!-- container -->
          <table width="600" cellpadding="0" cellspacing="0" role="presentation" style="max-width:600px;background:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 6px 30px rgba(16,24,40,0.08);">
            <!-- header -->
            <tr>
              <td style="padding:24px 30px 10px;text-align:center;background:linear-gradient(90deg,#6610f2,#8f50ff);color:#fff;">
                <h1 style="margin:0;font-size:20px;font-weight:700;">MiniWiki</h1>
                <p style="margin:6px 0 0;font-size:13px;opacity:0.95;">Tasdiqlash kodi</p>
              </td>
            </tr>

            <!-- body -->
            <tr>
              <td style="padding:28px 30px;">
                <p style="margin:0 0 14px;color:#1f2937;font-size:25px;line-height:1.5;">
                  Salom <b>{user.fullname}</b> 👋,
                </p>

                <p style="margin:0 0 18px;color:#374151;font-size:20px;line-height:1.5;">
                  Sizning MiniWiki hisobingiz uchun tasdiqlash kodingiz:
                </p>

                <!-- code box -->
                <div style="margin:0 0 20px;text-align:center;">
                  <span style="display:inline-block;padding:18px 28px;border-radius:10px;background:#0ea5a3;color:#fff;font-weight:700;font-size:28px;letter-spacing:4px;">
                    {random_number}
                  </span>
                </div>

                <p style="margin:0 0 18px;color:#374151;font-size:20px;line-height:1.6;">
                  Ushbu kodni <strong>2 daqiqa</strong> ichida kiriting. Agar kodni so‘ramagan bo‘lsangiz, bu xabarni e’tiborsiz qoldiring.
                </p>

                <!-- CTA button -->
                

                <hr style="border:none;border-top:1px solid #eef2ff;margin:22px 0;">

                <p style="margin:0;color:#6b7280;font-size:12px;line-height:1.5;">
                  Agar siz ushbu so‘rovni amalga oshirmagan bo‘lsangiz — hisobot qiling yoki parolingizni o‘zgartiring.
                </p>
              </td>
            </tr>

            <!-- footer -->
            <tr>
              <td style="padding:16px 24px;background:#fafafa;text-align:center;font-size:12px;color:#9ca3af;">
                <h3 style = 'color:black;'>MiniWiki &middot; Sizning ishonchli ma'lumot manbangiz</h3><br>
               
              </td>
            </tr>
          </table>
          <!-- /container -->
        </td>
      </tr>
    </table>
  </body>
</html>
"""