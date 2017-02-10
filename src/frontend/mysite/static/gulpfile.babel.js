// Requis
var gulp = require('gulp');

// Include plugins
var plugins = require('gulp-load-plugins')(); // Inclu tous les plugins de package.json

var sass = require('gulp-sass'); //gulp-sass pas pris en charge par gulp-load-plugins

var browserSync = require('browser-sync').create();
var sourcemaps = require('gulp-sourcemaps');
var babel = require("gulp-babel");

// Tâche "sass" = SASS + autoprefixer + CSScomb + beautify
gulp.task('sass', function () {
     return gulp.src('css/sass/main.scss')
     .pipe(sourcemaps.init())
     .pipe(plugins.sass().on('error', sass.logError))
     .pipe(plugins.csscomb())
     .pipe(plugins.cssbeautify({indent: '   '}))
     .pipe(plugins.autoprefixer())
     .pipe(sourcemaps.write('.'))
     .pipe(gulp.dest('css/'))
     .pipe(browserSync.stream());
});

gulp.task("js", function () {
    return gulp.src("js/es/**/*.es")
        .pipe(sourcemaps.init())
        .pipe(babel())
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest("js/"));
});

// Tâche "minify" = minification CSS
gulp.task('minifyCSS', function () {
    return gulp.src(['css/*.css', '!css/*.min.css'])
        .pipe(plugins.csso())
        .pipe(plugins.rename({
             suffix: '.min'
         }))
        .pipe(gulp.dest('css/'));
});

// Tâche "optimizeImage" = compression des images
gulp.task('optimizeImage', function () {
	return gulp.src('img/*')
		.pipe(plugins.imagemin())
		.pipe(gulp.dest('img/'));
});


// Tâche "prod" = sass + minify + optimize
gulp.task('prod', ['sass', 'minifyCSS', 'optimizeImage']);

// Tâche "watch" = surveille modification et rafraichît navigateur
gulp.task('watch', function () {

  browserSync.init({
      proxy: "127.0.0.1:8000"
  });

  gulp.watch('css/sass/**/*.scss', browserSync.reload);
  gulp.watch('../myapps/**/*.scss', browserSync.reload);
  gulp.watch('js/**/*.es', browserSync.reload);
  gulp.watch('../myapps/**/*.es', browserSync.reload);
  gulp.watch('../templates/**/*.html', browserSync.reload);
  gulp.watch('../myapps/**/*.html', browserSync.reload);

  gulp.watch('js/es/**/*.es', ['js']);
  gulp.watch('css/sass/**/*.scss', ['sass']);
});

// Tâche par défaut
gulp.task('default', ['watch']);
