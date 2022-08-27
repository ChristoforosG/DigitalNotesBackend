# DigitaNotes Documentation

Το συγκεκριμένο πληροφοριακό σύστημα υλοποιήθηκε με χρήση της MongoDB ως βάση δεδομένων και το Flask της python για backend server. Επιπλέον η εργασία έγινε containerized χρησιμοποιώντας το Docker. Συνεπώς, για την εκτέλεση της εφαρμογής πρέπει να είναι εγκατεστημένο το Docker Desktop και ένα μέσο για την εκτέλεση των requests, όπως το Postman ή ένα command line tool. Για να εκκινήσει η εφαρμογή εκτελούμε την εντολή `docker-compose up` από το path που περιέχει το docker-compose.yml.

## Δομή του Back End

Στον φάκελο backend υπάρχουν τρία `.py` αρχεία. Το `app.py` που αποτελεί το main αρχείο του server, το `User.py` που περιέχει όλες τις συναρτήσεις που αφορούν ενέργειες του User και τέλος το `Notes_API.py` που περιέχει τις συναρτήσεις που αφορούν τις ενέργειες των σημειώσεων από τους χρήστες.

## Τα end points της εφαρμογής

Όλα τα end-points στα οποία μπορούμε να στείλουμε requests βρίσκονται στο αρχείο app.py στον φάκελο backend.

1. `@app.route('/sign-up', methods=['POST'])`

   Πραγματοποιεί εγγραφή νέου απλού χρήστη. Πρόκειται για ένα post request το οποίο υλοποιείται από την συνάρτηση `def sign_up(data)` στο module User.

2. `@app.route('/sign-in', methods=['POST'])`

   Πραγματοποιεί την είσοδο ενός χρήστη (είτε απλού χρήστη, είτε διαχειριστή) στην εφαρμογή. Πρόκειται για ένα post request το οποίο υλοποιείται από την συνάρτηση `def sign_in(data)` στο module User.

3. `@app.route('/notes-show', methods=["GET"])`

   Απαιτεί ο χρήστης να έχει συνεδεθεί στην εφαρμογή. Πραγματοποιεί εμφάνιση όλων των σημειώσεων του χρήστη με χρονολογική σειρά. Πρόκειται για ένα get request το οποίο υλοποιείται από την συνάρτηση `def notes_show()` στο module Notes_API.

4. `@app.route("/note-insert", methods=["POST"])`

   Απαιτεί ο χρήστης να έχει συνεδεθεί στην εφαρμογή. Δημιουργεί και εισάγει μια νέα σημείωση στην βάση. Πρόκειται για ένα post request το οποίο υλοποιείται από την συνάρτηση `def note_insert(data)` στο module Notes_API.

5. `@app.route("/note-search-title", methods=["GET"])`

   Απαιτεί ο χρήστης να έχει συνεδεθεί στην εφαρμογή. Πραγματοποιεί αναζήτηση μίας ή περισσοτέρων σημειώσεων βάσει τίτλου. Πρόκειται για ένα get request το οποίο υλοποιείται από την συνάρτηση `def note_search(key, value)` στο module Notes_API.

6. `@app.route("/note-search-keyword", methods=["GET"])`

   Απαιτεί ο χρήστης να έχει συνεδεθεί στην εφαρμογή. Πραγματοποιεί αναζήτηση μίας ή περισσοτέρων σημειώσεων βάσει λέξης κλειδιού. Πρόκειται για ένα get request το οποίο υλοποιείται από την συνάρτηση `def note_search(key, value)` στο module Notes_API.

7. `@app.route("/note-change/<string:title>", methods=["PUT"])`

   Απαιτεί ο χρήστης να έχει συνεδεθεί στην εφαρμογή. Πραγματοποιεί τροποποίηση μίας ή περισσότερων σημειώσεων βάσει τίτλου. Πρόκειται για ένα put request το οποίο υλοποιείται από την συνάρτηση `def note_change(title, data)` στο module Notes_API.

8. `@app.route("/note-delete", methods=["DELETE"])`

   Απαιτεί ο χρήστης να έχει συνεδεθεί στην εφαρμογή. Πραγματοποιεί διαγραφή μίας ή περισσότερων σημειώσεων βάσει τίτλου. Πρόκειται για ένα delete request το οποίο υλοποιείται από την συνάρτηση `def note_delete(title)` στο module Notes_API.

9. `@app.route("/user-delete", methods=["DELETE"])`

   Απαιτεί ο χρήστης να έχει συνεδεθεί στην εφαρμογή. Πραγματοποιεί διαγραφή του χρήστη και των σημειώσεων του. Πρόκειται για ένα delete request το οποίο υλοποιείται από την συνάρτηση `def user_delete()` στο module User.

10. `@app.route("/admin-delete/<user_name>", methods=["DELETE"])`

    Απαιτεί ο χρήστης να έχει συνεδεθεί στην εφαρμογή και να έχει ρόλο διαχειριστή. Πραγματοποιεί διαγραφή οποιουδήποτε λογαριασμού. Πρόκειται για ένα delete request το οποίο υλοποιείται από την συνάρτηση `def admin_delete(user_name)` στο module User.

11. `@app.route("/admin-add/", methods=["POST"])`

    Απαιτεί ο χρήστης να έχει συνεδεθεί στην εφαρμογή και να έχει ρόλο διαχειριστή. Πραγματοποιεί εγγραφή νέου χρήστη-διαχειριστή. Πρόκειται για ένα post request το οποίο υλοποιείται από την συνάρτηση `def admin_add(data)` στο module User.

## Αρχιτεκτονική Βάσης

Αρχικά στην MongoDB δημιουργήθηκε μια νέα βάση με όνομα DigitalNotes και σε αυτή την βάση δημιουργήθηκαν δύο documents (Πίνακες), ο `User` και ο `Note`. Ο πρώτος περιέχει στοιχεία για τους χρήστες και ο δεύτερος στοιχεία για τις σημειώσεις κάθε χρήστη. Συγκεκριμένα

1. `User`

```
{
    _id (Primary Key)
    user_name
    password
    e_mail
    name
    is_admin
}
```

2. `Note`

```
{
    _id (Primary Key)
    title
    text
    keywords
    date
    user
}
```

## Υλοποίηση συναρτήσεων

### User Module

1. `def access_db()`

   Δημιουργεί έναν MongoClient στην βάση δεδομένων DigitalNotes για να μπορούμε να πραγματοποιούμε queries. Χρησιμοποιείται από όλες τις συναρτήσεις.

2. `get_hash_value(value)`

   Δημιουργεί ένα hash value με χρήση του SHA256 ώστε να αποθηκεύουμε τον κωδικό κρυπτογραφημένο, για λόγους ασφάλειας.

3. `def sign_up(data)`

   Πραγματοποιεί δημιουργία λογαριασμού απλού χρήστη. Ελέγχει στον πίνακα User ότι δεν υπάρχει άλλος χρήστης με ίδιο email ή user name, Θέτει το `is_admin` με `False`, αφού πρόκειται για απλό χρήστη, δημιουργεί το hash value του κωδικού και με την βιβλιοθήκη `uuid` δημιουργεί το primary key. Τέλος, αποθηκεύει τον νέο χρήστη στην βάση.

4. `def sign_in(data)`

   Χρησιμοποιείται για την είσοδο του χρήστη στην εφαρμογή. Αρχικά ελέγχει εάν ο χρήστης προσπαθεί να εισέλθει με user name ή email, και στην συνέχεια αν βρεί αντίστοιχο χρήστη ελέγχει τα hash values των κωδικών εάν ταυτίζονται. Τέλος, συνδέει τον χρήστη και του επιστρέφει ένα access token (περισσότερα στην συνέχεια).

5. `def user_delete()`

   Η συγκεκριμένη συνάρτηση διαγράφει τον λογαριάσμο του χρήστη που την εκτέλεσε καθώς και τις σημειώσεις του.

6. `def is_admin(user)`

   Γίνεται έλεγχος εάν ο χρήστης είναι διαχειριστής ή όχι.

7. `def admin_delete(user_name)`

   Η συγκεκριμένη συνάρτηση, αφού πιστοποιήσει ότι ο χρήστης είναι διαχειριστής, διαγράφεί τον χρήστη με βάσει το user_name που δόθηκε, και τις αντίστοιχες σημειώσεις.

8. `def admin_add(data)`

   Η συγκεκριμένη συνάρτηση, αφού πιστοποιήσει ότι ο χρήστης είναι διαχειριστής, δημιουργεί έναν νέο διαχειριστή. Αρχικά ελέγχει ότι εχουν δοθεί όλα τα απαραίτητα πεδία στο request, δημιουργεί το `_id` και εάν τα user name και email είναι μοναδικά, δημιουργεί τον νέο διαχειριστή.

### Notes_API Module

1. `def notes_show()`

   Η συγκεκριμένη συνάρτηση, βρίκσκει το `_id` του χρήστη από το access_token. Στην συνέχεια πραγματοποιεί αναζήτηση των σημειώσεων του χρήστη και τα εμφανίζει με χρόνολογική σειρά ξεκινώντας από το πιο πρόσφατο.

2. `def note_insert(data)`

   Η συγκεκριμένη συνάρτηση αρχικά ελέγχει πως ο χρήστης έχει δώσει σώστα όλα τα απαραίτητα πεδία στο request και στην συνέχεια το `_id` του user στο πεδίο `user` και την ημερομηνία εκχώρησης στο πεδίο `date`. Στην συνέχεια κάνει insert στον πίνακα `Note` την σημείωση.

3. `def note_delete(title)`

   Η συγκεκριμένη συνάρτηση ελέγχει ότι ο χρήστης έχει σημειώσεις με τίτλο `title` και αν βρεί τις διαγράφει όλες.

4. `def note_search(key, value)`

   Η συγκεκριμένη συνάρτηση πραγματοποιεί αναζήτηση με βάσει τον τίτλο, εάν `key = "title"` ή με βάσει μια λέξη κλειδί, εάν `key = "keyword"`. Στην συνέχεια πραγματοποιεί την αναζήτηση των σημειώσεων και τις επιστρέφει. Προσοχή, στην περίπτωση του keyword γίνεται έλεγχος εάν η λέξη κλειδί ανήκει στην λίστα των λέξεων κλειδιών της σημείωσης.

5. `def note_change(title, data)`

   Η συγκεκριμένη συνάρτηση αρχικά ελέγχει εάν το request έχει όλα τα απαραίτητα πεδία και στην συνέχεια ελέγχει ότι ο χρήστης έχει σημειώσεις με τίτλο `title`. Εάν βρεί τις διαγράφει όλες.

## Πιστοποίηση συνδεδεμένου χρήστη

Για να ελέγξουμε πως ο χρήστης έχει συνδεθεί στην εφαρμογή χρήσιμοποιήσαμε την βιβλιοθήκη `flask-jwt-extended` με την οποία δημιουργείται ένα token κατά την σύνδεση, το οποίο παράγεται από ένα κρύφο κλειδί που το γνωρίζει μόνο η εφαρμογή και είναι μοναδικό για κάθε χρήστη. Το token αυτό μπορεί να γίνει decode και να προκύψει το id του χρήστη, το οποίο και χρήσιμοποιούμε στις παραπάνω συναρτήσεις. Το token έχει συγκεκριμένο χρόνο ζωής και κάθε φορά που λήγει απαιτείται ο χρήστης να ξανασυνδεθεί. Τα end points τα οποία απαιτούν ο χρήστης να έχει συνδεθεί έχουν έναν decorator και συγκεκριμένα: `@jwt_required(fresh=True)`.

## Παραδείγματα Εκτέλεσης

### Δημιουργία πρώτου διαχεριστή

### Εκτέλση των end points

1. Δημιουργία Λογαργιασμού
   Request Type: POST
   Request URL: `http://localhost:5000/sign-up`
   BODY: `{"user_name": "", "password": "", "e_mail": "", "name": ""}`
2. Είσοδος στον λογαργιασμό
   Request Type: POST
   Request URL: `http://localhost:5000/sign-in`
   BODY: `{"user_name": "", "password": ""}`
3. Προσθήκη σημείωσης
   Request Type: POST
   Request URL: `http://localhost:5000/note-insert`
   Authorization: Bearer Token
   BODY: `{"title": "", "text": "", "keywords": ""}`
4. Αναζήτηση σημείωσης βάσει τίτλου
   Request Type: GET
   Request URL: `http://localhost:5000/note-search-title?title={}`
   Authorization: Bearer Token
5. Αναζήτηση σημείωσης βάσει λέξης κλειδιού
   Request Type: GET
   Request URL: `http://localhost:5000/note-search-keyword?keyword={}`
   Authorization: Bearer Token
6. Τροποποίηση σημείωσης
   Request Type: PUT
   Request URL: `http://localhost:5000/note-change/{}`
   BODY: {"title": "", ""text": "", "keywords": ""}
   Authorization: Bearer Token
7. Εμφάνιση Σημειώσεων
   Request Type: GET
   Request URL: http://localhost:5000/notes-show
   Authorization: Bearer Token
8. Διαγραφή Σημείωσης βάσει τίτλου
   Request Type: DELETE
   Request URL: `http://localhost:5000/note-delete?tile={}`
   Authorization: Bearer Token
9. Εγγραφή νέου διαχειριστή
   Request Type: POST
   Request URL: `http://localhost:5000/admin-add`
   BODY: `{"user_name": "", "password": "", "e_mail": "", "name": ""}`
   Authorization: Bearer Token
10. Διαγραφή οποιουδήποτε λογαριασμού
    Request Type: DELETE
    Request URL: `http://localhost:5000/admin-delete/{}`
    Authorization: Bearer Token
11. Διαγραφή λογαριασμού
    Request Type: DELETE
    Request URL: `http://localhost:5000/user-delete`
    Authorization: Bearer Token
