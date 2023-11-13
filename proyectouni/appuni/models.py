from django.db import models


class Alumno(models.Model):
    MATERIAS = (
        ("Programación lógica", "Programación lógica"),
        ("Algebra", "Algebra"),
        ("Programación Orientada a Objetos", "Programación Orientada a Objetos"),
        ("Administración I", "Administración I"),
        ("Contabilidad", "Contabilidad"),
        ("Principios de economía", "Principios de economía"),
        ("Introducción al derecho", "Introducción al derecho"),
        ("Teoría de la Persona", "Teoría de la Persona"),
        ("Derecho Penal I", "Derecho Penal I"),        
    )


    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    materia = models.CharField(max_length=128, choices=MATERIAS)