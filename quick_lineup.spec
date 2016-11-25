# -*- mode: python -*-

block_cipher = None


a = Analysis(['quick_lineup.py'],
             pathex=['Z:\\teamy-quick-lineup'],
             binaries=None,
             datas=None,
             hiddenimports=['html.parser','http.cookies',
                            'django.template.defaulttags','django.template.loader_tags',
                            'django.middleware.common',
                            'ql.settings',
                            'mysql.connector.django', 'mysql.connector.django.base',
                            'mysql.connector.django.compiler'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='quick_lineup',
          debug=False,
          strip=False,
          upx=True,
          console=True )
