import os

thing = {
    "TOKEN": "MTAwNjEzNTQ2Mjg1NzAyMzU1OA.GJ3ZXm._1bj76yaS2XRYoa31inAYRrhhlvzWCLpnTb2Cg",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "client_email": "firebase-adminsdk-zwj2w@opus-db287.iam.gserviceaccount.com",
    "client_id": "113277906607434287853",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-zwj2w%40opus-db287.iam.gserviceaccount.com",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCVQ5iPtlw+DzOv\nWq1WjX0ZLo71KKfVm+MCJe2YriBfUgXRlkeKCBXCJYp7Z82GRg1k4NEK/HROK4Mt\n6UOsPN5C5Z+fXK9/qfv7nt15dTGid5jIN2WvXFpfdCy0bre6Xw6yGhd49xicBLmG\nDFgxnKoWybXxUojTGODCirv8sxmFV4/L7XtH/EI0e+joGv1UcCW9c9q3MCfX9bq7\nufBxyosAD/O+v/MIL0wR41LXnqglI9nh3cbTv0+7CM+ANk/ls3fNDMtEzZaJypZ5\naUu+EScpri4/RRncRxZCkzksJy5vapXdUW89lQSFEXdz+F7AdOwbhLqeqXk7wzEt\ncEyR+C63AgMBAAECggEAK+XHVmyhUDcUUjvuwoe2BNPmgz9DrNS9vIH/EGoVZzMu\nNudlfrjF/WUhBw4OKbEse0CK+hoo8lxlpfj2SA9WpoH1od6WVotdajDcnb3TrR5T\nNn7kTuBwS6ZVB3OQYSVXoxV9VbwF5syU61FyFpUmiLEl6yUEzGCCqXQ3uSfLF6Wn\nzVSyZ2vxuifKajYVMCVTHhnz3rC6NHud+sCl9dGZ9Yj5gyhr4zJw82Mi/UbXLUXe\n/SO8rb8JeGkLMWouhqy5ypJJAGjvZH1iurEO6051l+ek0SSL3Sr2v4Jzmn6Ki4/d\nLIxwUMTlhSrvDVzd4ITDYEUEftF6c6qnzjrMPX/WcQKBgQDGHEYgFL4XqTYKaHw5\nZQ8V/eHXhHIHbvxIFCwx8taPO3/S7pjhFtn8yckIqvFDVNquu9QniPYFRts56eon\ncBhPG/0I69v9VuU4qO9KpGcnifAS+m9pl1VE0MMeduT30LKWqxEWur7Hyp+7LgAJ\nRPimPYAB8xHE6fxATfYH8cV1UwKBgQDA4VlQXEDjFbSwEGpcrTouYnLF9YELHbGP\nC/wixRat61xrkC/LvQYX0VUmtKmCZ5vOepvO0o9kH0xgqjqgW/R2Pfvr27GpK+0A\nM2eggfa0SGjMjGhIkO8cFXxwSR0QDBriyykXLGg7DcwGRwigv0TceRhyzvMzkt8Y\nSFhrPw0wjQKBgDl5WGrUObXZlGD+oRNxmyfRKOUCeqZnb29l0tCG1/Jj25iROe8L\nVyB8VgNavHXBN1Q8D7eMh3tObCloEFNytMq2nvkonADqZcPDVvC7s2WIIgsPdqUW\nj1lQi1raOWEfvb/yTxneAZ0qzp5aIQ6PYOexreJi50POci0hsP/rB1MbAoGBAKko\nuhD9Z7cBQV+sdevjzQQDOY+eGdeq6h9/rli8K4DKy1pWsWRo2iAnahuxFH0W6xGy\nfFVuW22++VhJ03LyUrsk731SR0UMDiY/7yFY+gnw+2Bxv7/sxJgHzAQaS0/YnffL\nn7UAMEWiew4CXHHGbdlCpwuBrs/LfreoM0uTl7i9AoGAV23jP0TJFk7Zw3u0rX+1\n+cQWX1CgrzUJqMOdqIqYLJ61/V+9Add6afmuOP1eJlZr1HW1hVA3ty4fm1WR3FTG\nPpPbMPU3RmsjlpIMazghhNqgnTtizTFX5MDT7Ao4LcFH6VA7MNNHOEsIf8nJ9KZQ\nlJC1MlXpPudZo/B+ceQkors=\n-----END PRIVATE KEY-----\n",
    "private_key_id": "2ad69a04b04a6ff2807378f5d03746cb6ae809ca",
    "project_id": "opus-db287",
    "token_uri": "https://oauth2.googleapis.com/token",
    "type": "service_account",
}

for key, value in thing.items():
    os.system(f"$env:{key} = '{value}'")
