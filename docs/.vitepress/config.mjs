import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "D-Jà Vue",
  description: "Documentação Oficial do Djàvue",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      //{ text: 'Examples', link: '/markdown-examples' }
    ],

    sidebar: [
      {
        text: 'Documentação',
        items: [
          { text: '🤔 O que é', link: '/intro' },
          { text: '💿 Instalação', link: '/instalacao' },
          { text: '👶 Iniciando', link: '/iniciando' },
          { text: '🚀 Deploy ', link: '/deploy' },
          { text: '👾 Contribuindo', link: '/contribuindo' },
          { text: '📝 CHANGELOG', link: '/changelog' },
          { text: '🇬🇧 English', link: '/README_EN' },
          { text: '🇧🇷 Português', link: '/README_PT' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/evolutio/djavue3' },
      { icon: 'youtube', link: 'https://www.youtube.com/watch?v=pDYvJIxxoN0&list=PL1Skk6O-pP7vRPCWmzMYXNEkx4BMZlhgi' }
    ]
  }
})
