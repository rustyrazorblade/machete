
module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        coffee: {
            compile: {
                files: {
                        'static/js/machete.js': ['static/coffeescript/*.coffee'] // compile and concat into single file
                }
            }
        }

    });

    // Load the plugin that provides the "uglify" task.
    //grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-coffee');

    // Default task(s).
    //grunt.registerTask('default', ['uglify']);

};
