Instructions for Database:
1. Create a database called 'project'
2. Run the sql following sql command in the new database: 'CREATE TABLE `projects` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255),
    `description` VARCHAR(255),
    `created_at` DATETIME,
    `status` VARCHAR(32),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB;'

Instructions for Flask Server:
1. In the root of the project server folder run 'pip install -r requirements.txt' from the command line
2. Run 'export FLASK_APP=index.py'
3. Run 'flask run'