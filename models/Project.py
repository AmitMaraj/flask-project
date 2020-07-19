class Project():
    name = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(255), nullable = True)
    status = db.Column(db.String(12), nullable = True)
    created_at = db.Column(db.Date(), nullable = True)
        