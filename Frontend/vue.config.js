module.exports = {
  // 放置生成的静态资源的（outputDir）目录， outputDir就是生产环境构建文件的目录名设置
  assetsDir: 'static',
  // 是否为 Babel 或 TypeScript 使用 thread-loader。
  parallel: false,
  // 开发、部署时的 URL
  publicPath: './',
  devServer: {
    // true 则热更新，false 则手动刷新，默认值为 true
    disableHostCheck: true,
    inline: false,
    // development server port 8000
  },
  server: {
    hmr: {
      protocol: 'ws',
      host: 'localhost',
    },
  },

}
