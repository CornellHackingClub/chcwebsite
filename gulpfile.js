var gulp        = require('gulp');
var browserSync = require('browser-sync');
var sass 	    = require('gulp-sass');
var reload      = browserSync.reload;

gulp.task('sass', function () {
  return gulp.src('./**/*.{sass,scss}')
     // .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('.'));
});

gulp.task('default', function() {
    browserSync.init({
        notify: false,
        proxy: "localhost:8000"
    });
    gulp.watch('./**/*.{sass,scss}',['sass']);
    gulp.watch(['./**/*.{sass,scss,css,html,py,js,cd,ts}'], reload);
});
