const path = require('path');

module.exports = {
  entry: './src/scripts.js', // 入口文件
  output: { // 输出文件
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
  },
  mode: 'production', // 打包模式
};
