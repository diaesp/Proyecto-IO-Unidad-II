<?php
  session_start();
  include("conexion.php");
  include("logIn.php");
?>

<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Academia de música PRODIGIOS - Clases de piano, guitarra, canto, violín y más instrumentos. Aprende música con los mejores instructores.">
  <meta name="keywords" content="música, clases, piano, guitarra, canto, violín, ukelele, requinto, academia">
  <title>PRODIGIOS - Academia de Música | Clases de Instrumentos Musicales</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/index.css">
</head>
<body>
  <!-- Encabezado -->
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark">
      <div class="container">
        <a class="navbar-brand" href="index_01.php" aria-label="PRODIGIOS - Inicio">PRODIGIOS</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto">
            <li class="nav-item"><a class="nav-link" href="#inicio" aria-label="Ir a sección Inicio">Inicio</a></li>
            <li class="nav-item"><a class="nav-link" href="#cursos" aria-label="Ir a sección Cursos">Cursos</a></li>
            <li class="nav-item"><a class="nav-link" href="#instructores" aria-label="Ir a sección Instructores">Instructores</a></li>
            <li class="nav-item"><a class="nav-link" href="#contacto" aria-label="Ir a sección Contacto">Contacto</a></li>
          </ul>
          <div class="d-flex">
            <button class="btn btn-outline-light me-2" data-bs-toggle="modal" data-bs-target="#modalLogin" aria-label="Abrir modal de inicio de sesión">Iniciar Sesión</button>
            <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalRegistro" aria-label="Abrir modal de registro">Registrarse</button>
          </div>
        </div>
      </div>
    </nav>
  </header>

  <!-- Sección de Carrusel -->
  <section id="inicio" class="mb-5">
    <div id="mainCarousel" class="carousel slide carousel-fade" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#mainCarousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#mainCarousel" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#mainCarousel" data-bs-slide-to="2" aria-label="Slide 3"></button>
        <button type="button" data-bs-target="#mainCarousel" data-bs-slide-to="3" aria-label="Slide 4"></button>
        <button type="button" data-bs-target="#mainCarousel" data-bs-slide-to="4" aria-label="Slide 5"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="5000">
          <img src="../assets/img/image1.jpg" class="d-block w-100" alt="Persona tocando requinto" loading="lazy">
          <div class="carousel-caption d-none d-md-block">
            <h3>Clases de Requinto</h3>
            <p>Aprende técnicas profesionales con nuestros instructores certificados</p>
          </div>
        </div>
        <div class="carousel-item" data-bs-interval="5000">
          <img src="../assets/img/image2.jpg" class="d-block w-100" alt="Persona tocando piano" loading="lazy">
          <div class="carousel-caption d-none d-md-block">
            <h3>Clases de Piano</h3>
            <p>Desde principiantes hasta niveles avanzados</p>
          </div>
        </div>
        <div class="carousel-item" data-bs-interval="5000">
          <img src="../assets/img/image3.jpg" class="d-block w-100" alt="Persona tocando ukelele" loading="lazy">
          <div class="carousel-caption d-none d-md-block">
            <h3>Clases de Ukelele</h3>
            <p>El instrumento perfecto para comenzar en la música</p>
          </div>
        </div>
        <div class="carousel-item" data-bs-interval="5000">
          <img src="../assets/img/image4.jpg" class="d-block w-100" alt="Persona cantando" loading="lazy">
          <div class="carousel-caption d-none d-md-block">
            <h3>Clases de Canto</h3>
            <p>Desarrolla tu voz con técnicas profesionales</p>
          </div>
        </div>
        <div class="carousel-item" data-bs-interval="5000">
          <img src="../assets/img/image5.jpg" class="d-block w-100" alt="Persona tocando guitarra" loading="lazy">
          <div class="carousel-caption d-none d-md-block">
            <h3>Clases de Guitarra</h3>
            <p>Aprende tus canciones favoritas desde el primer día</p>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#mainCarousel" data-bs-slide="prev" aria-label="Slide anterior">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Anterior</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#mainCarousel" data-bs-slide="next" aria-label="Slide siguiente">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Siguiente</span>
      </button>
    </div>
  </section>

  <!-- Sección de Cursos -->
  <section id="cursos" class="section-padding bg-light courses-section">
    <div class="container">
      <h2 class="text-center mb-5">Nuestros Cursos</h2>
        <!-- Filtros de cursos -->
        <div class="course-filter">
          <button class="filter-btn active" data-filter="all">Todos</button>
          <button class="filter-btn" data-filter="piano">Piano</button>
          <button class="filter-btn" data-filter="guitarra">Guitarra</button>
          <button class="filter-btn" data-filter="canto">Canto</button>
          <button class="filter-btn" data-filter="violin">Violín</button>
          <button class="filter-btn" data-filter="ukelele">Ukelele</button>
          <button class="filter-btn" data-filter="requinto">Requinto</button>
        </div>
        <!-- Grid de cursos -->
        <div class="courses-container">
          <!-- Curso de Piano -->
          <div class="course-card" data-category="piano">
            <img src="../assets/img/piano.jpg" alt="Clases de piano" class="course-img">
            <div class="course-content">
            <span class="course-category">Piano</span>
            <h3 class="course-title">Piano para Principiantes</h3>
            <p class="course-description">Aprende las bases del piano y desarrolla tu técnica con nuestro método progresivo.</p>
            <div class="course-meta">
              <span class="course-price">S/. 120</span>
              <span class="course-duration">12 clases</span>
            </div>
            <a href="#" class="btn-enroll" data-bs-toggle="modal" data-bs-target="#pianoModal">Más información</a>
            </div>
          </div>
          <!-- Curso de Guitarra -->
          <div class="course-card" data-category="guitarra">
            <img src="../assets/img/guitarra.jpg" alt="Clases de guitarra" class="course-img">
            <div class="course-content">
            <span class="course-category">Guitarra</span>
            <h3 class="course-title">Guitarra Moderna</h3>
            <p class="course-description">Domina acordes, escalas y técnicas para tocar tus canciones favoritas.</p>
            <div class="course-meta">
              <span class="course-price">S/. 100</span>
              <span class="course-duration">8 clases</span>
            </div>
            <a href="#" class="btn-enroll" data-bs-toggle="modal" data-bs-target="#guitarraModal">Más información</a>
            </div>
          </div>
          <!-- Curso de Canto -->
          <div class="course-card" data-category="canto">
            <img src="../assets/img/canto.jpg" alt="Clases de canto" class="course-img">
            <div class="course-content">
            <span class="course-category">Canto</span>
            <h3 class="course-title">Técnica Vocal</h3>
            <p class="course-description">Desarrolla tu voz con ejercicios de respiración, afinación y proyección.</p>
            <div class="course-meta">
              <span class="course-price">S/. 90</span>
              <span class="course-duration">10 clases</span>
            </div>
            <a href="#" class="btn-enroll" data-bs-toggle="modal" data-bs-target="#cantoModal">Más información</a>
            </div>
          </div>
          <!-- Curso de Violín -->
          <div class="course-card" data-category="violin">
            <img src="../assets/img/violin.jpg" alt="Clases de violín" class="course-img">
            <div class="course-content">
            <span class="course-category">Violín</span>
            <h3 class="course-title">Violín Clásico</h3>
            <p class="course-description">Aprende la técnica correcta del violín con repertorio clásico y moderno.</p>
            <div class="course-meta">
              <span class="course-price">S/. 150</span>
              <span class="course-duration">12 clases</span>
            </div>
            <a href="#" class="btn-enroll" data-bs-toggle="modal" data-bs-target="#violinModal">Más información</a>
            </div>
          </div>
          <!-- Curso de Ukelele -->
          <div class="course-card" data-category="ukelele">
            <img src="../assets/img/ukelele.jpg" alt="Clases de ukelele" class="course-img">
            <div class="course-content">
            <span class="course-category">Ukelele</span>
            <h3 class="course-title">Ukelele Divertido</h3>
            <p class="course-description">El instrumento perfecto para comenzar en la música de forma alegre.</p>
            <div class="course-meta">
              <span class="course-price">S/. 80</span>
              <span class="course-duration">8 clases</span>
            </div>
            <a href="#" class="btn-enroll" data-bs-toggle="modal" data-bs-target="#ukeleleModal">Más información</a>
            </div>
          </div>
          <!-- Curso de Requinto -->
          <div class="course-card" data-category="requinto">
            <img src="../assets/img/requinto.jpg" alt="Clases de requinto" class="course-img">
            <div class="course-content">
            <span class="course-category">Requinto</span>
            <h3 class="course-title">Requinto Tradicional</h3>
            <p class="course-description">Domina este instrumento melódico esencial en la música tradicional.</p>
            <div class="course-meta">
              <span class="course-price">S/. 110</span>
              <span class="course-duration">10 clases</span>
            </div>
            <a href="#" class="btn-enroll" data-bs-toggle="modal" data-bs-target="#requintoModal">Más información</a>
            </div>
          </div>
        </div>
    </div>
  </section>

  <!-- Sección de Instructores -->
  <section id="instructores" class="section-padding">
    <div class="container">
      <h2 class="text-center mb-5">Nuestros Instructores</h2>
      <div class="row g-4">
        
        <!-- Instructor 1 -->
        <div class="col-md-6 col-lg-4">
          <div class="card h-100">
            <div class="card-body text-center p-4">
              <img src="../assets/img/user.jpg" class="instructor-img rounded-circle mb-4" alt="Instructor Juan Pérez" loading="lazy">
              <h3 class="card-title">Juan Pérez</h3>
              <p class="text-muted"><i class="fas fa-piano me-2"></i> Piano</p>
              <p class="card-text">Pianista con más de 15 años de experiencia en enseñanza y presentaciones en vivo. Graduado del Conservatorio Nacional de Música.</p>
              <div class="mt-3">
                <a href="#" class="btn btn-outline-primary btn-sm me-2" data-bs-toggle="modal" data-bs-target="#instructorModal1">Ver perfil</a>
                <a href="#" class="btn btn-primary btn-sm">Contactar</a>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Instructor 2 -->
        <div class="col-md-6 col-lg-4">
          <div class="card h-100">
            <div class="card-body text-center p-4">
              <img src="../assets/img/user.jpg" class="instructor-img rounded-circle mb-4" alt="Instructora Ana Gómez" loading="lazy">
              <h3 class="card-title">Ana Gómez</h3>
              <p class="text-muted"><i class="fas fa-microphone me-2"></i> Canto</p>
              <p class="card-text">Cantante profesional con 10 años de experiencia en enseñanza vocal. Especializada en técnica vocal contemporánea.</p>
              <div class="mt-3">
                <a href="#" class="btn btn-outline-primary btn-sm me-2" data-bs-toggle="modal" data-bs-target="#instructorModal2">Ver perfil</a>
                <a href="#" class="btn btn-primary btn-sm">Contactar</a>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Instructor 3 -->
        <div class="col-md-6 col-lg-4">
          <div class="card h-100">
            <div class="card-body text-center p-4">
              <img src="../assets/img/user.jpg" class="instructor-img rounded-circle mb-4" alt="Instructor Pedro López" loading="lazy">
              <h3 class="card-title">Pedro López</h3>
              <p class="text-muted"><i class="fas fa-guitar me-2"></i> Guitarra</p>
              <p class="card-text">Guitarrista profesional con amplia experiencia en géneros como rock, blues y jazz. Ha participado en múltiples giras internacionales.</p>
              <div class="mt-3">
                <a href="#" class="btn btn-outline-primary btn-sm me-2" data-bs-toggle="modal" data-bs-target="#instructorModal3">Ver perfil</a>
                <a href="#" class="btn btn-primary btn-sm">Contactar</a>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Instructor 4 -->
        <div class="col-md-6 col-lg-4">
          <div class="card h-100">
            <div class="card-body text-center p-4">
              <img src="../assets/img/user.jpg" class="instructor-img rounded-circle mb-4" alt="Instructora María Fernández" loading="lazy">
              <h3 class="card-title">María Fernández</h3>
              <p class="text-muted"><i class="fas fa-music me-2"></i> Violín</p>
              <p class="card-text">Violinista clásica con formación en el extranjero. Miembro de la Orquesta Sinfónica Nacional por más de 8 años.</p>
              <div class="mt-3">
                <a href="#" class="btn btn-outline-primary btn-sm me-2" data-bs-toggle="modal" data-bs-target="#instructorModal4">Ver perfil</a>
                <a href="#" class="btn btn-primary btn-sm">Contactar</a>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Instructor 5 -->
        <div class="col-md-6 col-lg-4">
          <div class="card h-100">
            <div class="card-body text-center p-4">
              <img src="../assets/img/user.jpg" class="instructor-img rounded-circle mb-4" alt="Instructora Luisa Rodríguez" loading="lazy">
              <h3 class="card-title">Luisa Rodríguez</h3>
              <p class="text-muted"><i class="fas fa-guitar me-2"></i> Ukelele</p>
              <p class="card-text">Especialista en música hawaiana y contemporánea con el ukelele. Más de 5 años enseñando a niños y adultos.</p>
              <div class="mt-3">
                <a href="#" class="btn btn-outline-primary btn-sm me-2" data-bs-toggle="modal" data-bs-target="#instructorModal5">Ver perfil</a>
                <a href="#" class="btn btn-primary btn-sm">Contactar</a>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Instructor 6 -->
        <div class="col-md-6 col-lg-4">
          <div class="card h-100">
            <div class="card-body text-center p-4">
              <img src="../assets/img/user.jpg" class="instructor-img rounded-circle mb-4" alt="Instructor Carlos Méndez" loading="lazy">
              <h3 class="card-title">Carlos Méndez</h3>
              <p class="text-muted"><i class="fas fa-guitar me-2"></i> Requinto</p>
              <p class="card-text">Experto en música tradicional y requinto. Ha participado en festivales internacionales de música folklórica.</p>
              <div class="mt-3">
                <a href="#" class="btn btn-outline-primary btn-sm me-2" data-bs-toggle="modal" data-bs-target="#instructorModal6">Ver perfil</a>
                <a href="#" class="btn btn-primary btn-sm">Contactar</a>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="text-center mt-5">
        <button class="btn btn-outline-primary">Ver todos los instructores</button>
      </div>
    </div>
  </section>

  <!-- Sección de Testimonios Premium -->
  <section class="testimonials-section">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Testimonios</h2>
      </div>

      <div id="premiumTestimonials" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <!-- Testimonio 1 - Piano -->
          <div class="carousel-item active">
            <div class="row justify-content-center">
              <div class="col-lg-8">
                <div class="testimonial-card">
                  <div class="quote-icon">
                    <i class="fas fa-quote-right"></i>
                  </div>
                  <div class="testimonial-content">
                    <p class="testimonial-text">Las clases de piano en PRODIGIOS han revolucionado mi aprendizaje. En 6 meses logré dominar piezas de Chopin que nunca pensé posibles. La paciencia de los instructores y su enfoque personalizado son incomparables.</p>
                    
                    <div class="testimonial-author">
                      <div class="author-image">
                        <img src="../assets/img/user.jpg" alt="Sofía Martínez">
                      </div>
                      <div class="author-info">
                        <h3 class="author-name">Sofía Martínez</h3>
                        <p class="author-details">Estudiante de <span>Piano</span> · 9 meses</p>
                        <div class="rating">
                          <i class="fas fa-star"></i>
                          <i class="fas fa-star"></i>
                          <i class="fas fa-star"></i>
                          <i class="fas fa-star"></i>
                          <i class="fas fa-star"></i>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Testimonio 2 - Guitarra -->
          <div class="carousel-item">
            <div class="row justify-content-center">
              <div class="col-lg-8">
                <div class="testimonial-card">
                  <div class="quote-icon">
                    <i class="fas fa-quote-right"></i>
                  </div>
                  <div class="testimonial-content">
                    <p class="testimonial-text">Como adulto que soñaba con aprender guitarra, pensé que sería imposible. En PRODIGIOS diseñaron un plan adaptado a mi ritmo. Hoy toco mis canciones favoritas y compongo mis propias melodías. ¡Una experiencia transformadora!</p>
                    
                    <div class="testimonial-author">
                      <div class="author-image">
                        <img src="../assets/img/user.jpg" alt="Javier López">
                      </div>
                      <div class="author-info">
                        <h3 class="author-name">Javier López</h3>
                        <p class="author-details">Estudiante de <span>Guitarra</span> · 1 año</p>
                        <div class="rating">
                          <i class="fas fa-star"></i>
                          <i class="fas fa-star"></i>
                          <i class="fas fa-star"></i>
                          <i class="fas fa-star"></i>
                          <i class="fas fa-star-half-alt"></i>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Testimonio 3 - Canto -->
          <div class="carousel-item">
            <div class="row justify-content-center">
              <div class="col-lg-8">
                <div class="testimonial-card">
                  <div class="quote-icon">
                    <i class="fas fa-quote-right"></i>
                  </div>
                  <div class="testimonial-content">
                    <p class="testimonial-text">Las clases de canto no solo mejoraron mi técnica vocal, sino que transformaron mi confianza personal. La metodología me ayudó a entender mi rango vocal y prepararme para audiciones. ¡Gané un concurso de talentos gracias a lo aprendido!</p>
                    
                    <div class="testimonial-author">
                      <div class="author-image">
                        <img src="../assets/img/user.jpg" alt="Valeria Ramírez">
                      </div>
                      <div class="author-info">
                        <h3 class="author-name">Valeria Ramírez</h3>
                        <p class="author-details">Estudiante de <span>Canto</span> · 1.5 años</p>
                        <div class="rating">
                          <i class="fas fa-star"></i>
                          <i class="fas fa-star"></i>
                          <i class="fas fa-star"></i>
                          <i class="fas fa-star"></i>
                          <i class="far fa-star"></i>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Testimonio 4 - Violín -->
          <div class="carousel-item">
            <div class="row justify-content-center">
              <div class="col-lg-8">
                <div class="testimonial-card">
                  <div class="quote-icon">
                    <i class="fas fa-quote-right"></i>
                  </div>
                  <div class="testimonial-content">
                    <p class="testimonial-text">Cuando comencé con violín a los 35 años pensé que sería demasiado tarde. Mi instructor adaptó las lecciones a mi ritmo y hoy toco en un ensamble local. Las clases personalizadas y el ambiente de apoyo hacen toda la diferencia.</p>
                    
                    <div class="testimonial-author">
                      <div class="author-image">
                        <img src="../assets/img/user.jpg" alt="Carlos Mendoza">
                      </div>
                      <div class="author-info">
                        <h3 class="author-name">Carlos Mendoza</h3>
                        <p class="author-details">Estudiante de <span>Violín</span> · 1 año</p>
                        <div class="rating">
                          <i class="fas fa-star"></i>
                          <i class="fas fa-star"></i>
                          <i class="fas fa-star"></i>
                          <i class="fas fa-star"></i>
                          <i class="fas fa-star"></i>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Controles del carrusel - Solo para esta sección -->
        <button class="carousel-control-prev" type="button" data-bs-target="#premiumTestimonials" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Anterior</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#premiumTestimonials" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Siguiente</span>
        </button>

        <!-- Indicadores - Solo para esta sección -->
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#premiumTestimonials" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#premiumTestimonials" data-bs-slide-to="1" aria-label="Slide 2"></button>
          <button type="button" data-bs-target="#premiumTestimonials" data-bs-slide-to="2" aria-label="Slide 3"></button>
          <button type="button" data-bs-target="#premiumTestimonials" data-bs-slide-to="3" aria-label="Slide 4"></button>
        </div>
      </div>
    </div>
  </section>

  <!-- Sección de Contacto -->
  <section id="contacto" class="section-padding">
    <div class="container">
      <h2 class="text-center mb-5">Contáctanos</h2>
      <div class="row g-4">
        <!-- Información de Contacto -->
        <div class="col-lg-4">
          <div class="card border-0 shadow-sm h-100">
            <div class="card-body p-4">
              <h3 class="mb-4">Información de Contacto</h3>
              
              <div class="d-flex mb-4">
                <div class="me-3 text-primary">
                  <i class="fas fa-map-marker-alt fa-2x"></i>
                </div>
                <div>
                  <h5 class="mb-1">Dirección</h5>
                  <p class="mb-0">LA ESPERANZA, Brasil 1318, Tacna 23001</p>
                </div>
              </div>
              
              <div class="d-flex mb-4">
                <div class="me-3 text-primary">
                  <i class="fas fa-phone-alt fa-2x"></i>
                </div>
                <div>
                  <h5 class="mb-1">Teléfono</h5>
                  <p class="mb-0">995522159</p>
                </div>
              </div>
              
              <div class="d-flex mb-4">
                <div class="me-3 text-primary">
                  <i class="fas fa-envelope fa-2x"></i>
                </div>
                <div>
                  <h5 class="mb-1">Email</h5>
                  <p class="mb-0">info@prodigios.edu.pe</p>
                </div>
              </div>
              
              <div class="d-flex mb-4">
                <div class="me-3 text-primary">
                  <i class="fas fa-clock fa-2x"></i>
                </div>
                <div>
                  <h5 class="mb-1">Horario de Atención</h5>
                  <p class="mb-0">Lunes a Viernes: 9am - 8pm<br>Sábados: 9am - 2pm</p>
                </div>
              </div>
              
              <div class="mt-4">
                <h5 class="mb-3">Síguenos</h5>
                <div class="d-flex">
                  <a href="https://www.facebook.com/AcademiadeMusicaProdigios" target="_blank" class="text-decoration-none me-3" aria-label="Facebook de PRODIGIOS">
                    <i class="fab fa-facebook-f fa-2x"></i>
                  </a>
                  <a href="#" class="text-decoration-none me-3" target="_blank" aria-label="Instagram de PRODIGIOS">
                    <i class="fab fa-instagram fa-2x"></i>
                  </a>
                  <a href="#" class="text-decoration-none me-3" target="_blank" aria-label="YouTube de PRODIGIOS">
                    <i class="fab fa-youtube fa-2x"></i>
                  </a>
                  <a href="#" class="text-decoration-none" target="_blank" aria-label="TikTok de PRODIGIOS">
                    <i class="fab fa-tiktok fa-2x"></i>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Mapa -->
        <div class="col-lg-4">
          <div class="card border-0 shadow-sm h-100">
            <div class="card-body p-0">
              <div class="map-container">
                <iframe src="https://www.google.com/maps/embed?pb=!1m12!1m8!1m3!1d30357.258085875143!2d-70.247902!3d-17.994676!3m2!1i1024!2i768!4f13.1!2m1!1sprodigios!5e0!3m2!1ses!2spe!4v1750286873071!5m2!1ses!2spe" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Formulario de Contacto -->
        <div class="col-lg-4">
          <div class="card border-0 shadow-sm h-100">
            <div class="card-body p-4">
              <h3 class="mb-4">Envíanos un Mensaje</h3>
              <form id="contactForm" class="needs-validation" novalidate action="https://formspree.io/f/mldledqd" method="POST">
                <div class="mb-3">
                  <label for="name" class="form-label">Nombre Completo</label>
                  <input type="text" class="form-control" id="name" required>
                  <div class="invalid-feedback">
                    Por favor ingresa tu nombre.
                  </div>
                </div>
                
                <div class="mb-3">
                  <label for="email" class="form-label">Email</label>
                  <input type="email" class="form-control" id="email" required>
                  <div class="invalid-feedback">
                    Por favor ingresa un email válido.
                  </div>
                </div>
                
                <div class="mb-3">
                  <label for="phone" class="form-label">Teléfono (Opcional)</label>
                  <input type="tel" class="form-control" id="phone">
                </div>
                
                <div class="mb-3">
                  <label for="subject" class="form-label">Asunto</label>
                  <select class="form-select" id="subject" required>
                    <option value="" selected disabled>Selecciona un asunto</option>
                    <option value="informacion">Información sobre cursos</option>
                    <option value="inscripcion">Inscripciones</option>
                    <option value="instructores">Información sobre instructores</option>
                    <option value="otro">Otro</option>
                  </select>
                  <div class="invalid-feedback">
                    Por favor selecciona un asunto.
                  </div>
                </div>
                
                <div class="mb-3">
                  <label for="message" class="form-label">Mensaje</label>
                  <textarea class="form-control" id="message" rows="4" required></textarea>
                  <div class="invalid-feedback">
                    Por favor escribe tu mensaje.
                  </div>
                </div>
                
                <div class="d-grid">
                  <button type="submit" class="btn btn-primary">Enviar Mensaje</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Pie de página -->
  <footer class="py-5">
    <div class="container">
      <div class="row">
        
        <div class="col-lg-4 mb-4 mb-lg-0">
          <h3 class="text-white mb-4">PRODIGIOS</h3>
          <p>La academia de música donde descubrirás y desarrollarás tu talento musical con los mejores instructores y metodologías.</p>
          <div class="social-icons">
            <a href="https://www.facebook.com/AcademiadeMusicaProdigios" target="_blank" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
            <a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
            <a href="#" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
            <a href="#" aria-label="Spotify"><i class="fab fa-spotify"></i></a>
          </div>
        </div>
        
        <div class="col-lg-2 col-md-6 mb-4 mb-md-0">
          <h4 class="text-white mb-4">Cursos</h4>
          <ul class="list-unstyled">
            <li class="mb-2"><a href="#" class="text-white-50 text-decoration-none" data-bs-toggle="modal" data-bs-target="#pianoModal">Piano</a></li>
            <li class="mb-2"><a href="#" class="text-white-50 text-decoration-none" data-bs-toggle="modal" data-bs-target="#guitarraModal">Guitarra</a></li>
            <li class="mb-2"><a href="#" class="text-white-50 text-decoration-none" data-bs-toggle="modal" data-bs-target="#cantoModal">Canto</a></li>
            <li class="mb-2"><a href="#" class="text-white-50 text-decoration-none" data-bs-toggle="modal" data-bs-target="#violinModal">Violín</a></li>
            <li><a href="#cursos" class="text-white-50 text-decoration-none">Ver todos</a></li>
          </ul>
        </div>
        
        <div class="col-lg-2 col-md-6 mb-4 mb-md-0">
          <h4 class="text-white mb-4">Enlaces</h4>
          <ul class="list-unstyled">
            <li class="mb-2"><a href="#inicio" class="text-white-50 text-decoration-none">Inicio</a></li>
            <li class="mb-2"><a href="#cursos" class="text-white-50 text-decoration-none">Cursos</a></li>
            <li class="mb-2"><a href="#instructores" class="text-white-50 text-decoration-none">Instructores</a></li>
            <li class="mb-2"><a href="#contacto" class="text-white-50 text-decoration-none">Contacto</a></li>
            <li><a href="#" class="text-white-50 text-decoration-none">Blog</a></li>
          </ul>
        </div>
        
        <div class="col-lg-4">
          <h4 class="text-white mb-4">Newsletter</h4>
          <p>Suscríbete para recibir noticias sobre nuevos cursos, eventos y promociones.</p>
          <form class="mb-3">
            <div class="input-group">
              <input type="email" class="form-control" placeholder="Tu email" aria-label="Tu email" required>
              <button class="btn btn-primary" type="submit">Suscribirse</button>
            </div>
          </form>
          <small class="text-white-50">Respetamos tu privacidad. Nunca compartiremos tu información.</small>
        </div>
      </div>
      
      <hr class="my-4 bg-light">
      
      <div class="row align-items-center">
        <div class="col-md-6 text-center text-md-start">
          <p class="mb-0">&copy; 2024 Academia de Música PRODIGIOS. Todos los derechos reservados.</p>
        </div>
        <div class="col-md-6 text-center text-md-end">
          <a href="#" class="text-white-50 text-decoration-none me-3">Términos y Condiciones</a>
          <a href="#" class="text-white-50 text-decoration-none">Política de Privacidad</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Botón para volver arriba -->
  <a href="#" class="back-to-top" aria-label="Volver arriba">
    <i class="fas fa-arrow-up"></i>
  </a>

  <!-- Modal Iniciar Sesión -->
  <div class="modal fade" id="modalLogin" tabindex="-1" aria-labelledby="modalLoginLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header text-white" style="background: #2c4d90">
          <h5 class="modal-title" id="modalLoginLabel">Iniciar Sesión</h5>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form id="loginForm" method="post" novalidate>
            <div class="mb-3">
              <label for="loginEmail" class="form-label">Email</label>
              <input type="email" class="form-control" id="loginEmail" name="emailLogin" required>
              <div class="invalid-feedback">
                Por favor ingresa un email válido.
              </div>
            </div>
            <div class="mb-3">
              <label for="loginPassword" class="form-label">Contraseña</label>
              <input type="password" class="form-control" id="loginPassword" name="passwordLogin" required>
              <div class="invalid-feedback">
                Por favor ingresa tu contraseña.
              </div>
            </div>
            <div class="mb-3 form-check">
              <input type="checkbox" class="form-check-input" id="rememberMe">
              <label class="form-check-label" for="rememberMe">Recordarme</label>
            </div>
            <div class="d-grid mb-3">
              <button type="submit" class="btn btn-primary">Iniciar Sesión</button>
            </div>
            <div class="text-center">
              <a href="#" class="text-decoration-none" data-bs-toggle="modal" data-bs-target="#modalForgotPassword" data-bs-dismiss="modal">¿Olvidaste tu contraseña?</a>
            </div>
          </form>
        </div>
        <div class="modal-footer justify-content-center">
          <p class="mb-0">¿No tienes una cuenta? <a href="#" class="text-decoration-none" data-bs-toggle="modal" data-bs-target="#modalRegistro" data-bs-dismiss="modal">Regístrate</a></p>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal Registrarse -->
  <div class="modal fade" id="modalRegistro" tabindex="-1" aria-labelledby="modalRegistroLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header text-white" style="background:#2c4d90">
          <h5 class="modal-title" id="modalRegistroLabel">Crear Cuenta</h5>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form id="registerForm" method="post" class="needs-validation" novalidate>
            <div class="row">
              <div class="col-md-6 mb-3">
                <label for="firstName" class="form-label">Nombres</label>
                <input type="text" class="form-control" id="firstName" name="nombreRegistro" required>
                <div class="invalid-feedback">
                  Por favor ingresa tus nombres.
                </div>
              </div>
              <div class="col-md-6 mb-3">
                <label for="lastName" class="form-label">Apellidos</label>
                <input type="text" class="form-control" id="lastName" name="apellidoRegistro" required>
                <div class="invalid-feedback">
                  Por favor ingresa tus apellidos.
                </div>
              </div>
            </div>
            
            <div class="mb-3">
              <label for="registerEmail" class="form-label">Email</label>
              <input type="email" class="form-control" id="registerEmail" name="emailRegistro" required>
              <div class="invalid-feedback">
                Por favor ingresa un email válido.
              </div>
            </div>
            
            <div class="mb-3">
              <label for="registerPhone" class="form-label">Teléfono</label>
              <input type="tel" class="form-control" id="registerPhone" name="telefonoRegistro" required>
              <div class="invalid-feedback">
                Por favor ingresa tu número telefónico.
              </div>
            </div>
            
            <div class="mb-3">
              <label for="registerPassword" class="form-label">Contraseña</label>
              <input type="password" class="form-control" id="registerPassword" name="passwordRegistro" required>
              <div class="invalid-feedback">
                Por favor crea una contraseña.
              </div>
            </div>
            
            <div class="mb-3">
              <label for="confirmPassword" class="form-label">Confirmar Contraseña</label>
              <input type="password" class="form-control" id="confirmPassword" name="passwordRegistro1" required>
              <div class="invalid-feedback">
                Las contraseñas deben coincidir.
              </div>
            </div>
            
            <div class="mb-3 form-check">
              <input type="checkbox" class="form-check-input" id="acceptTerms" required>
              <label class="form-check-label" for="acceptTerms" style="color: #333;">Acepto los <a href="#" class="text-decoration-none">Términos y Condiciones</a> y la <a href="#" class="text-decoration-none">Política de Privacidad</a></label>
              <div class="invalid-feedback">
                Debes aceptar los términos y condiciones.
              </div>
            </div>
            
            <div class="d-grid">
              <button type="submit" class="btn btn-primary">Registrarse</button>
            </div>
          </form>
        </div>
        <div class="modal-footer justify-content-center">
          <p class="mb-0">¿Ya tienes una cuenta? <a href="#" class="text-decoration-none" data-bs-toggle="modal" data-bs-target="#modalLogin" data-bs-dismiss="modal">Inicia Sesión</a></p>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal Recuperar Contraseña -->
  <div class="modal fade" id="modalForgotPassword" tabindex="-1" aria-labelledby="modalForgotPasswordLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header text-white" style="background: #2c4d90">
          <h5 class="modal-title" id="modalForgotPasswordLabel">Recuperar Contraseña</h5>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <p>Ingresa tu email y te enviaremos un enlace para restablecer tu contraseña.</p>
          <form id="forgotPasswordForm" novalidate>
            <div class="mb-3">
              <label for="forgotEmail" class="form-label">Email</label>
              <input type="email" class="form-control" id="forgotEmail" required>
              <div class="invalid-feedback">
                Por favor ingresa un email válido.
              </div>
            </div>
            <div class="d-grid">
              <button type="submit" class="btn btn-primary">Enviar Enlace</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal Instructor 1: Juan Pérez -->
  <div class="modal fade" id="instructorModal1" tabindex="-1" aria-labelledby="instructorModal1Label" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header text-white" style="background: #2c4d90;">
          <h5 class="modal-title" id="instructorModal1Label">Juan Pérez - Instructor de Piano</h5>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-5 text-center">
              <img src="../assets/img/user.jpg" class="img-fluid rounded-circle mb-4" alt="Instructor Juan Pérez" loading="lazy" style="width: 200px; height: 200px; object-fit: cover;">
              <div class="mb-4">
                <h5>Especialidades</h5>
                <span class="badge bg-primary me-1 mb-1">Piano Clásico</span>
                <span class="badge bg-primary me-1 mb-1">Jazz</span>
                <span class="badge bg-primary me-1 mb-1">Composición</span>
              </div>
              <div class="mb-4">
                <h5>Idiomas</h5>
                <p>Español, Inglés, Francés</p>
              </div>
              <div>
                <h5>Contacto</h5>
                <p>juan.perez@prodigios.edu.pe</p>
              </div>
            </div>
            <div class="col-md-7">
              <h4 class="mb-3">Biografía</h4>
              <p>Juan Pérez es un pianista con más de 15 años de experiencia en enseñanza y presentaciones en vivo. Graduado del Conservatorio Nacional de Música con honores, ha participado en festivales internacionales en Europa y América.</p>
              <p>Su método de enseñanza se basa en la técnica clásica adaptada a los intereses y habilidades de cada estudiante, fomentando siempre la creatividad y el amor por la música.</p>
              
              <h4 class="mb-3 mt-4">Experiencia</h4>
              <ul class="list-unstyled">
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Profesor en Conservatorio Nacional (2015-2020)</li>
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Pianista en Orquesta Sinfónica de Lima (2012-2018)</li>
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Ganador del Concurso Internacional de Piano (2010)</li>
              </ul>
              
              <h4 class="mb-3 mt-4">Horarios Disponibles</h4>
              <div class="row">
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Lunes</small>
                      <p class="mb-0">9am - 12pm</p>
                    </div>
                  </div>
                </div>
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Miércoles</small>
                      <p class="mb-0">2pm - 6pm</p>
                    </div>
                  </div>
                </div>
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Viernes</small>
                      <p class="mb-0">10am - 3pm</p>
                    </div>
                  </div>
                </div>
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Sábado</small>
                      <p class="mb-0">9am - 1pm</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Cerrar</button>
          <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalRegistro" data-bs-dismiss="modal">Inscribirme con este instructor</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal Instructor 2: Ana Gómez -->
  <div class="modal fade" id="instructorModal2" tabindex="-1" aria-labelledby="instructorModal2Label" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header text-white" style="background: #2c4d90;">
          <h5 class="modal-title" id="instructorModal2Label">Ana Gómez - Instructora de Canto</h5>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-5 text-center">
              <img src="../assets/img/user.jpg" class="img-fluid rounded-circle mb-4" alt="Instructora Ana Gómez" loading="lazy" style="width: 200px; height: 200px; object-fit: cover;">
              <div class="mb-4">
                <h5>Especialidades</h5>
                <span class="badge bg-primary me-1 mb-1">Técnica Vocal</span>
                <span class="badge bg-primary me-1 mb-1">Música Contemporánea</span>
                <span class="badge bg-primary me-1 mb-1">Interpretación</span>
              </div>
              <div class="mb-4">
                <h5>Idiomas</h5>
                <p>Español, Inglés</p>
              </div>
              <div>
                <h5>Contacto</h5>
                <p>ana.gomez@prodigios.edu.pe</p>
              </div>
            </div>
            <div class="col-md-7">
              <h4 class="mb-3">Biografía</h4>
              <p>Ana Gómez es una cantante profesional con 10 años de experiencia en enseñanza vocal. Especializada en técnica vocal contemporánea, ha entrenado a cantantes que hoy forman parte de agrupaciones profesionales y han ganado concursos nacionales.</p>
              <p>Su método de enseñanza se centra en desarrollar una base técnica sólida mientras se explora la expresión artística personal de cada estudiante.</p>
              
              <h4 class="mb-3 mt-4">Experiencia</h4>
              <ul class="list-unstyled">
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Vocal coach en "La Voz Perú" (2018-2020)</li>
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Cantante solista en Orquesta Sinfónica Nacional (2015-2019)</li>
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Ganadora del Festival de Canto Popular (2014)</li>
              </ul>
              
              <h4 class="mb-3 mt-4">Horarios Disponibles</h4>
              <div class="row">
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Martes</small>
                      <p class="mb-0">10am - 2pm</p>
                    </div>
                  </div>
                </div>
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Jueves</small>
                      <p class="mb-0">3pm - 7pm</p>
                    </div>
                  </div>
                </div>
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Sábado</small>
                      <p class="mb-0">9am - 1pm</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Cerrar</button>
          <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalRegistro" data-bs-dismiss="modal">Inscribirme con este instructor</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal Instructor 3: Pedro López -->
  <div class="modal fade" id="instructorModal3" tabindex="-1" aria-labelledby="instructorModal3Label" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header text-white" style="background: #2c4d90;">
          <h5 class="modal-title" id="instructorModal3Label">Pedro López - Instructor de Guitarra</h5>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-5 text-center">
              <img src="../assets/img/user.jpg" class="img-fluid rounded-circle mb-4" alt="Instructor Pedro López" loading="lazy" style="width: 200px; height: 200px; object-fit: cover;">
              <div class="mb-4">
                <h5>Especialidades</h5>
                <span class="badge bg-primary me-1 mb-1">Guitarra Eléctrica</span>
                <span class="badge bg-primary me-1 mb-1">Blues</span>
                <span class="badge bg-primary me-1 mb-1">Rock</span>
              </div>
              <div class="mb-4">
                <h5>Idiomas</h5>
                <p>Español, Inglés</p>
              </div>
              <div>
                <h5>Contacto</h5>
                <p>pedro.lopez@prodigios.edu.pe</p>
              </div>
            </div>
            <div class="col-md-7">
              <h4 class="mb-3">Biografía</h4>
              <p>Pedro López es un guitarrista profesional con amplia experiencia en géneros como rock, blues y jazz. Ha participado en múltiples giras internacionales y grabado con artistas reconocidos en la escena musical latinoamericana.</p>
              <p>Su enfoque de enseñanza combina técnica sólida con aplicación práctica, permitiendo a los estudiantes tocar música real desde las primeras clases.</p>
              
              <h4 class="mb-3 mt-4">Experiencia</h4>
              <ul class="list-unstyled">
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Guitarrista de gira con banda internacional (2017-2020)</li>
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Profesor en Berklee College of Music (2014-2016)</li>
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Ganador del concurso nacional de guitarra (2012)</li>
              </ul>
              
              <h4 class="mb-3 mt-4">Horarios Disponibles</h4>
              <div class="row">
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Lunes</small>
                      <p class="mb-0">4pm - 8pm</p>
                    </div>
                  </div>
                </div>
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Miércoles</small>
                      <p class="mb-0">4pm - 8pm</p>
                    </div>
                  </div>
                </div>
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Viernes</small>
                      <p class="mb-0">3pm - 7pm</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Cerrar</button>
          <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalRegistro" data-bs-dismiss="modal">Inscribirme con este instructor</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal Instructor 4: María Fernández -->
  <div class="modal fade" id="instructorModal4" tabindex="-1" aria-labelledby="instructorModal4Label" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header text-white" style="background: #2c4d90;">
          <h5 class="modal-title" id="instructorModal4Label">María Fernández - Instructora de Violín</h5>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-5 text-center">
              <img src="../assets/img/user.jpg" class="img-fluid rounded-circle mb-4" alt="Instructora María Fernández" loading="lazy" style="width: 200px; height: 200px; object-fit: cover;">
              <div class="mb-4">
                <h5>Especialidades</h5>
                <span class="badge bg-primary me-1 mb-1">Violín Clásico</span>
                <span class="badge bg-primary me-1 mb-1">Música de Cámara</span>
                <span class="badge bg-primary me-1 mb-1">Técnica de Arco</span>
              </div>
              <div class="mb-4">
                <h5>Idiomas</h5>
                <p>Español, Inglés, Francés</p>
              </div>
              <div>
                <h5>Contacto</h5>
                <p>maria.fernandez@prodigios.edu.pe</p>
              </div>
            </div>
            <div class="col-md-7">
              <h4 class="mb-3">Biografía</h4>
              <p>María Fernández es violinista clásica con formación en el Conservatorio de París. Como miembro de la Orquesta Sinfónica Nacional por más de 8 años, ha actuado en las principales salas de concierto del país y participado en festivales internacionales.</p>
              <p>Su método de enseñanza enfatiza la técnica correcta desde el inicio, combinada con el desarrollo de la expresión musical personal.</p>
              
              <h4 class="mb-3 mt-4">Experiencia</h4>
              <ul class="list-unstyled">
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Primera violinista en Orquesta Sinfónica Nacional (2015-presente)</li>
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Profesora en Conservatorio Nacional (2012-2015)</li>
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Ganadora del concurso Jóvenes Solistas (2010)</li>
              </ul>
              
              <h4 class="mb-3 mt-4">Horarios Disponibles</h4>
              <div class="row">
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Martes</small>
                      <p class="mb-0">9am - 1pm</p>
                    </div>
                  </div>
                </div>
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Jueves</small>
                      <p class="mb-0">9am - 1pm</p>
                    </div>
                  </div>
                </div>
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Sábado</small>
                      <p class="mb-0">10am - 2pm</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Cerrar</button>
          <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalRegistro" data-bs-dismiss="modal">Inscribirme con este instructor</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal Instructor 5: Luisa Rodríguez -->
  <div class="modal fade" id="instructorModal5" tabindex="-1" aria-labelledby="instructorModal5Label" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header text-white" style="background: #2c4d90;">
          <h5 class="modal-title" id="instructorModal5Label">Luisa Rodríguez - Instructora de Ukelele</h5>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-5 text-center">
              <img src="../assets/img/user.jpg" class="img-fluid rounded-circle mb-4" alt="Instructora Luisa Rodríguez" loading="lazy" style="width: 200px; height: 200px; object-fit: cover;">
              <div class="mb-4">
                <h5>Especialidades</h5>
                <span class="badge bg-primary me-1 mb-1">Música Hawaiana</span>
                <span class="badge bg-primary me-1 mb-1">Fingerstyle</span>
                <span class="badge bg-primary me-1 mb-1">Enseñanza para Niños</span>
              </div>
              <div class="mb-4">
                <h5>Idiomas</h5>
                <p>Español, Inglés</p>
              </div>
              <div>
                <h5>Contacto</h5>
                <p>luisa.rodriguez@prodigios.edu.pe</p>
              </div>
            </div>
            <div class="col-md-7">
              <h4 class="mb-3">Biografía</h4>
              <p>Luisa Rodríguez es especialista en música hawaiana y contemporánea con el ukelele. Con más de 5 años de experiencia enseñando a niños y adultos, ha desarrollado un método único que hace el aprendizaje divertido y efectivo para todas las edades.</p>
              <p>Su pasión por este instrumento se refleja en su enseñanza dinámica y en la creación de un ambiente de aprendizaje positivo.</p>
              
              <h4 class="mb-3 mt-4">Experiencia</h4>
              <ul class="list-unstyled">
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Instructora en festivales internacionales de ukelele (2018-presente)</li>
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Directora del programa "Ukelele en las Escuelas" (2016-2020)</li>
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Artista endorser de marcas reconocidas de ukelele</li>
              </ul>
              
              <h4 class="mb-3 mt-4">Horarios Disponibles</h4>
              <div class="row">
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Lunes</small>
                      <p class="mb-0">3pm - 6pm</p>
                    </div>
                  </div>
                </div>
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Miércoles</small>
                      <p class="mb-0">3pm - 6pm</p>
                    </div>
                  </div>
                </div>
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Viernes</small>
                      <p class="mb-0">3pm - 6pm</p>
                    </div>
                  </div>
                </div>
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Sábado</small>
                      <p class="mb-0">10am - 1pm</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Cerrar</button>
          <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalRegistro" data-bs-dismiss="modal">Inscribirme con este instructor</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal Instructor 6: Carlos Méndez -->
  <div class="modal fade" id="instructorModal6" tabindex="-1" aria-labelledby="instructorModal6Label" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header text-white" style="background: #2c4d90;">
          <h5 class="modal-title" id="instructorModal6Label">Carlos Méndez - Instructor de Requinto</h5>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-5 text-center">
              <img src="../assets/img/user.jpg" class="img-fluid rounded-circle mb-4" alt="Instructor Carlos Méndez" loading="lazy" style="width: 200px; height: 200px; object-fit: cover;">
              <div class="mb-4">
                <h5>Especialidades</h5>
                <span class="badge bg-primary me-1 mb-1">Música Tradicional</span>
                <span class="badge bg-primary me-1 mb-1">Técnica de Púa</span>
                <span class="badge bg-primary me-1 mb-1">Improvisación</span>
              </div>
              <div class="mb-4">
                <h5>Idiomas</h5>
                <p>Español</p>
              </div>
              <div>
                <h5>Contacto</h5>
                <p>carlos.mendez@prodigios.edu.pe</p>
              </div>
            </div>
            <div class="col-md-7">
              <h4 class="mb-3">Biografía</h4>
              <p>Carlos Méndez es un experto en música tradicional y requinto con más de 15 años de experiencia. Ha participado en festivales internacionales de música folklórica y grabado con importantes agrupaciones de música latinoamericana.</p>
              <p>Como instructor, se enfoca en transmitir las técnicas tradicionales mientras adapta el instrumento a contextos musicales contemporáneos, manteniendo siempre la esencia del requinto.</p>
              
              <h4 class="mb-3 mt-4">Experiencia</h4>
              <ul class="list-unstyled">
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Director musical de "Los Tradicionales" (2010-presente)</li>
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Ganador del Festival Internacional del Requinto (2015, 2018)</li>
                <li class="mb-2"><i class="fas fa-check-circle text-primary me-2"></i> Compositor de más de 50 obras para requinto</li>
              </ul>
              
              <h4 class="mb-3 mt-4">Horarios Disponibles</h4>
              <div class="row">
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Martes</small>
                      <p class="mb-0">2pm - 6pm</p>
                    </div>
                  </div>
                </div>
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Jueves</small>
                      <p class="mb-0">2pm - 6pm</p>
                    </div>
                  </div>
                </div>
                <div class="col-6 mb-2">
                  <div class="card bg-light">
                    <div class="card-body p-2 text-center">
                      <small>Sábado</small>
                      <p class="mb-0">9am - 1pm</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-outline-secondary" data-bs-dismiss="modal">Cerrar</button>
          <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalRegistro" data-bs-dismiss="modal">Inscribirme con este instructor</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal Piano -->
  <div class="modal fade course-modal" id="pianoModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Curso de Piano</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <img src="../assets/img/piano.jpg" alt="Curso de piano" class="course-details-img">
          
          <div class="course-tabs">
            <ul class="nav nav-tabs" id="pianoTab" role="tablist">
              <li class="nav-item" role="presentation">
                <button class="nav-link active" id="descripcion-tab" data-bs-toggle="tab" data-bs-target="#piano-descripcion" type="button" role="tab">Descripción</button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link" id="temario-tab" data-bs-toggle="tab" data-bs-target="#piano-temario" type="button" role="tab">Temario</button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link" id="instructor-tab" data-bs-toggle="tab" data-bs-target="#piano-instructor" type="button" role="tab">Instructor</button>
              </li>
            </ul>
            <div class="tab-content" id="pianoTabContent">
              <div class="tab-pane fade show active" id="piano-descripcion" role="tabpanel">
                <h4>Descripción del Curso</h4>
                <p>Este curso está diseñado para que aprendas a tocar piano desde cero o para perfeccionar tu técnica si ya tienes conocimientos previos. Trabajaremos en:</p>
                <ul class="course-features">
                  <li><i class="fas fa-check-circle"></i> Postura correcta y posición de manos</li>
                  <li><i class="fas fa-check-circle"></i> Lectura de partituras</li>
                  <li><i class="fas fa-check-circle"></i> Técnicas de digitación</li>
                  <li><i class="fas fa-check-circle"></i> Teoría musical aplicada</li>
                  <li><i class="fas fa-check-circle"></i> Repertorio clásico y contemporáneo</li>
                </ul>
              </div>
              <div class="tab-pane fade" id="piano-temario" role="tabpanel">
                <h4>Temario del Curso</h4>
                <div class="accordion" id="pianoTemarioAccordion">
                  <div class="accordion-item">
                    <h3 class="accordion-header" id="headingOne">
                      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true">
                        Módulo 1: Fundamentos
                      </button>
                    </h3>
                    <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne">
                      <div class="accordion-body">
                        <ul>
                          <li>Conociendo el piano</li>
                          <li>Posición correcta</li>
                          <li>Primeros ejercicios</li>
                          <li>Notas en el pentagrama</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                  <div class="accordion-item">
                    <h3 class="accordion-header" id="headingTwo">
                      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo">
                        Módulo 2: Técnica Básica
                      </button>
                    </h3>
                    <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo">
                      <div class="accordion-body">
                        <ul>
                          <li>Escalas mayores y menores</li>
                          <li>Acordes básicos</li>
                          <li>Ejercicios de independencia</li>
                          <li>Primeras piezas musicales</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                  <div class="accordion-item">
                    <h3 class="accordion-header" id="headingThree">
                      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree">
                        Módulo 3: Repertorio
                      </button>
                    </h3>
                    <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree">
                      <div class="accordion-body">
                        <ul>
                          <li>Piezas clásicas sencillas</li>
                          <li>Música popular</li>
                          <li>Improvisación básica</li>
                          <li>Preparación para presentación</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="piano-instructor" role="tabpanel">
                <div class="row align-items-center">
                  <div class="col-md-4 text-center">
                    <img src="../assets/img/user.jpg" alt="Instructor Juan Pérez" class="img-fluid rounded-circle mb-3" style="width: 150px; height: 150px; object-fit: cover;">
                    <h5>Juan Pérez</h5>
                    <p class="text-muted">Instructor de Piano</p>
                  </div>
                  <div class="col-md-8">
                    <h4>Sobre el instructor</h4>
                    <p>Juan es un pianista con más de 15 años de experiencia en enseñanza y presentaciones en vivo. Graduado del Conservatorio Nacional de Música con honores, ha participado en festivales internacionales en Europa y América.</p>
                    <p>Su método de enseñanza se basa en la técnica clásica adaptada a los intereses y habilidades de cada estudiante, fomentando siempre la creatividad y el amor por la música.</p>
                    <div class="mt-3">
                      <span class="badge bg-primary me-1">Piano Clásico</span>
                      <span class="badge bg-primary me-1">Jazz</span>
                      <span class="badge bg-primary me-1">Improvisación</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="text-center mt-4">
            <a href="#" class="btn btn-primary btn-lg" data-bs-toggle="modal" data-bs-target="#modalRegistro">Inscribirse al Curso</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal Guitarra -->
  <div class="modal fade course-modal" id="guitarraModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Curso de Guitarra</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <img src="../assets/img/guitarra.jpg" alt="Curso de guitarra" class="course-details-img">
          
          <div class="course-tabs">
            <ul class="nav nav-tabs" id="guitarraTab" role="tablist">
              <li class="nav-item" role="presentation">
                <button class="nav-link active" id="guitarra-descripcion-tab" data-bs-toggle="tab" data-bs-target="#guitarra-descripcion" type="button" role="tab">Descripción</button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link" id="guitarra-temario-tab" data-bs-toggle="tab" data-bs-target="#guitarra-temario" type="button" role="tab">Temario</button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link" id="guitarra-instructor-tab" data-bs-toggle="tab" data-bs-target="#guitarra-instructor" type="button" role="tab">Instructor</button>
              </li>
            </ul>
            <div class="tab-content" id="guitarraTabContent">
              <div class="tab-pane fade show active" id="guitarra-descripcion" role="tabpanel">
                <h4>Descripción del Curso</h4>
                <p>Aprende a tocar guitarra desde cero o mejora tu técnica con nuestro curso completo que cubre todos los estilos:</p>
                <ul class="course-features">
                  <li><i class="fas fa-check-circle"></i> Acordes básicos y avanzados</li>
                  <li><i class="fas fa-check-circle"></i> Técnicas de rasgueo y punteo</li>
                  <li><i class="fas fa-check-circle"></i> Escalas y teoría aplicada</li>
                  <li><i class="fas fa-check-circle"></i> Improvisación</li>
                  <li><i class="fas fa-check-circle"></i> Mantenimiento del instrumento</li>
                </ul>
              </div>
              <div class="tab-pane fade" id="guitarra-temario" role="tabpanel">
                <h4>Temario del Curso</h4>
                <p>El curso se divide en 4 módulos progresivos que te llevarán desde lo más básico hasta técnicas avanzadas:</p>
                <ol>
                  <li><strong>Introducción a la guitarra:</strong> Partes del instrumento, afinación, primeros acordes</li>
                  <li><strong>Técnica básica:</strong> Rasgueos, cambios de acordes, canciones sencillas</li>
                  <li><strong>Desarrollo musical:</strong> Escalas, arpegios, teoría aplicada</li>
                  <li><strong>Estilos y repertorio:</strong> Rock, blues, folk, fingerstyle</li>
                </ol>
              </div>
              <div class="tab-pane fade" id="guitarra-instructor" role="tabpanel">
                <div class="row align-items-center">
                  <div class="col-md-4 text-center">
                    <img src="../assets/img/user.jpg" alt="Instructor Pedro López" class="img-fluid rounded-circle mb-3" style="width: 150px; height: 150px; object-fit: cover;">
                    <h5>Pedro López</h5>
                    <p class="text-muted">Instructor de Guitarra</p>
                  </div>
                  <div class="col-md-8">
                    <h4>Sobre el instructor</h4>
                    <p>Pedro es un guitarrista profesional con amplia experiencia en géneros como rock, blues y jazz. Ha participado en múltiples giras internacionales y grabado con artistas reconocidos.</p>
                    <p>Su enfoque de enseñanza combina técnica sólida con aplicación práctica, permitiendo a los estudiantes tocar música real desde las primeras clases.</p>
                    <div class="mt-3">
                      <span class="badge bg-primary me-1">Rock</span>
                      <span class="badge bg-primary me-1">Blues</span>
                      <span class="badge bg-primary me-1">Improvisación</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="text-center mt-4">
            <a href="#" class="btn btn-primary btn-lg" data-bs-toggle="modal" data-bs-target="#modalRegistro">Inscribirse al Curso</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal Canto -->
  <div class="modal fade course-modal" id="cantoModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Curso de Canto</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <img src="../assets/img/canto.jpg" alt="Curso de canto" class="course-details-img">
          
          <div class="course-tabs">
            <ul class="nav nav-tabs" id="cantoTab" role="tablist">
              <li class="nav-item" role="presentation">
                <button class="nav-link active" id="canto-descripcion-tab" data-bs-toggle="tab" data-bs-target="#canto-descripcion" type="button" role="tab">Descripción</button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link" id="canto-temario-tab" data-bs-toggle="tab" data-bs-target="#canto-temario" type="button" role="tab">Temario</button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link" id="canto-instructor-tab" data-bs-toggle="tab" data-bs-target="#canto-instructor" type="button" role="tab">Instructor</button>
              </li>
            </ul>
            <div class="tab-content" id="cantoTabContent">
              <div class="tab-pane fade show active" id="canto-descripcion" role="tabpanel">
                <h4>Descripción del Curso</h4>
                <p>Descubre y desarrolla tu voz con nuestro curso de canto profesional. Aprenderás:</p>
                <ul class="course-features">
                  <li><i class="fas fa-check-circle"></i> Técnica vocal correcta</li>
                  <li><i class="fas fa-check-circle"></i> Respiración diafragmática</li>
                  <li><i class="fas fa-check-circle"></i> Afinación y rango vocal</li>
                  <li><i class="fas fa-check-circle"></i> Interpretación y expresión</li>
                  <li><i class="fas fa-check-circle"></i> Cuidado de la voz</li>
                </ul>
                <p>El curso incluye grabaciones profesionales para que puedas escuchar tu progreso.</p>
              </div>
              <div class="tab-pane fade" id="canto-temario" role="tabpanel">
                <h4>Temario del Curso</h4>
                <div class="row">
                  <div class="col-md-6">
                    <h5>Fundamentos</h5>
                    <ul>
                      <li>Anatomía de la voz</li>
                      <li>Ejercicios de respiración</li>
                      <li>Calentamiento vocal</li>
                      <li>Postura correcta</li>
                    </ul>
                  </div>
                  <div class="col-md-6">
                    <h5>Técnica Vocal</h5>
                    <ul>
                      <li>Resonancia y proyección</li>
                      <li>Extensión del rango vocal</li>
                      <li>Vibrato y efectos</li>
                      <li>Estilos musicales</li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="canto-instructor" role="tabpanel">
                <div class="row align-items-center">
                  <div class="col-md-4 text-center">
                    <img src="../assets/img/user.jpg" alt="Instructora Ana Gómez" class="img-fluid rounded-circle mb-3" style="width: 150px; height: 150px; object-fit: cover;">
                    <h5>Ana Gómez</h5>
                    <p class="text-muted">Instructora de Canto</p>
                  </div>
                  <div class="col-md-8">
                    <h4>Sobre la instructora</h4>
                    <p>Ana es una cantante profesional con 10 años de experiencia en enseñanza vocal. Especializada en técnica vocal contemporánea, ha entrenado a cantantes que hoy forman parte de agrupaciones profesionales.</p>
                    <p>Su método combina técnica clásica con aplicaciones modernas, adaptándose a las necesidades de cada estudiante.</p>
                    <div class="mt-3">
                      <span class="badge bg-primary me-1">Técnica Vocal</span>
                      <span class="badge bg-primary me-1">Interpretación</span>
                      <span class="badge bg-primary me-1">Música Popular</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="text-center mt-4">
            <a href="#" class="btn btn-primary btn-lg" data-bs-toggle="modal" data-bs-target="#modalRegistro">Inscribirse al Curso</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal Violín -->
  <div class="modal fade course-modal" id="violinModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Curso de Violín</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <img src="../assets/img/violin.jpg" alt="Curso de violín" class="course-details-img">
          
          <div class="course-tabs">
            <ul class="nav nav-tabs" id="violinTab" role="tablist">
              <li class="nav-item" role="presentation">
                <button class="nav-link active" id="violin-descripcion-tab" data-bs-toggle="tab" data-bs-target="#violin-descripcion" type="button" role="tab">Descripción</button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link" id="violin-temario-tab" data-bs-toggle="tab" data-bs-target="#violin-temario" type="button" role="tab">Temario</button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link" id="violin-instructor-tab" data-bs-toggle="tab" data-bs-target="#violin-instructor" type="button" role="tab">Instructor</button>
              </li>
            </ul>
            <div class="tab-content" id="violinTabContent">
              <div class="tab-pane fade show active" id="violin-descripcion" role="tabpanel">
                <h4>Descripción del Curso</h4>
                <p>Domina el arte del violín con nuestro curso diseñado para todos los niveles. Aprenderás:</p>
                <ul class="course-features">
                  <li><i class="fas fa-check-circle"></i> Técnica correcta de arco y mano izquierda</li>
                  <li><i class="fas fa-check-circle"></i> Afinación y postura profesional</li>
                  <li><i class="fas fa-check-circle"></i> Vibrato y expresividad musical</li>
                  <li><i class="fas fa-check-circle"></i> Repertorio clásico y moderno</li>
                  <li><i class="fas fa-check-circle"></i> Lectura de partituras para violín</li>
                </ul>
              </div>
              <div class="tab-pane fade" id="violin-temario" role="tabpanel">
                <h4>Temario del Curso</h4>
                <div class="accordion" id="violinTemarioAccordion">
                  <div class="accordion-item">
                    <h3 class="accordion-header" id="violinHeadingOne">
                      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#violinCollapseOne" aria-expanded="true">
                        Módulo 1: Fundamentos
                      </button>
                    </h3>
                    <div id="violinCollapseOne" class="accordion-collapse collapse show" aria-labelledby="violinHeadingOne">
                      <div class="accordion-body">
                        <ul>
                          <li>Partes del violín y cuidado</li>
                          <li>Sujeción correcta del arco</li>
                          <li>Posición de manos y cuerpo</li>
                          <li>Primeras notas y escalas</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                  <div class="accordion-item">
                    <h3 class="accordion-header" id="violinHeadingTwo">
                      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#violinCollapseTwo">
                        Módulo 2: Técnica Intermedia
                      </button>
                    </h3>
                    <div id="violinCollapseTwo" class="accordion-collapse collapse" aria-labelledby="violinHeadingTwo">
                      <div class="accordion-body">
                        <ul>
                          <li>Cambios de posición</li>
                          <li>Doble cuerdas y acordes</li>
                          <li>Técnicas de arco: legato, staccato</li>
                          <li>Piezas clásicas nivel intermedio</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                  <div class="accordion-item">
                    <h3 class="accordion-header" id="violinHeadingThree">
                      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#violinCollapseThree">
                        Módulo 3: Avanzado y Estilos
                      </button>
                    </h3>
                    <div id="violinCollapseThree" class="accordion-collapse collapse" aria-labelledby="violinHeadingThree">
                      <div class="accordion-body">
                        <ul>
                          <li>Vibrato y expresividad avanzada</li>
                          <li>Música folklórica y contemporánea</li>
                          <li>Improvisación</li>
                          <li>Preparación para conciertos</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="violin-instructor" role="tabpanel">
                <div class="row align-items-center">
                  <div class="col-md-4 text-center">
                    <img src="../assets/img/user.jpg" alt="Instructora María Fernández" class="img-fluid rounded-circle mb-3" style="width: 150px; height: 150px; object-fit: cover;">
                    <h5>María Fernández</h5>
                    <p class="text-muted">Instructora de Violín</p>
                  </div>
                  <div class="col-md-8">
                    <h4>Sobre la instructora</h4>
                    <p>María es violinista clásica con formación en el extranjero y miembro de la Orquesta Sinfónica Nacional por más de 8 años. Su experiencia incluye participación en festivales internacionales y grabaciones profesionales.</p>
                    <p>Su método de enseñanza combina la técnica clásica con un enfoque moderno y accesible para estudiantes de todos los niveles.</p>
                    <div class="mt-3">
                      <span class="badge bg-primary me-1">Violín Clásico</span>
                      <span class="badge bg-primary me-1">Técnica de Arco</span>
                      <span class="badge bg-primary me-1">Música de Cámara</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="text-center mt-4">
            <a href="#" class="btn btn-primary btn-lg" data-bs-toggle="modal" data-bs-target="#modalRegistro">Inscribirse al Curso</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal Ukelele -->
  <div class="modal fade course-modal" id="ukeleleModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Curso de Ukelele</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <img src="../assets/img/ukelele.jpg" alt="Curso de ukelele" class="course-details-img">
          
          <div class="course-tabs">
            <ul class="nav nav-tabs" id="ukeleleTab" role="tablist">
              <li class="nav-item" role="presentation">
                <button class="nav-link active" id="ukelele-descripcion-tab" data-bs-toggle="tab" data-bs-target="#ukelele-descripcion" type="button" role="tab">Descripción</button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link" id="ukelele-temario-tab" data-bs-toggle="tab" data-bs-target="#ukelele-temario" type="button" role="tab">Temario</button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link" id="ukelele-instructor-tab" data-bs-toggle="tab" data-bs-target="#ukelele-instructor" type="button" role="tab">Instructor</button>
              </li>
            </ul>
            <div class="tab-content" id="ukeleleTabContent">
              <div class="tab-pane fade show active" id="ukelele-descripcion" role="tabpanel">
                <h4>Descripción del Curso</h4>
                <p>Disfruta aprendiendo música con el ukelele, el instrumento perfecto para principiantes. En este curso aprenderás:</p>
                <ul class="course-features">
                  <li><i class="fas fa-check-circle"></i> Afinación y primeros acordes</li>
                  <li><i class="fas fa-check-circle"></i> Ritmos y patrones de rasgueo</li>
                  <li><i class="fas fa-check-circle"></i> Técnicas de fingerpicking</li>
                  <li><i class="fas fa-check-circle"></i> Canciones populares y hawaianas</li>
                  <li><i class="fas fa-check-circle"></i> Mantenimiento básico del instrumento</li>
                </ul>
              </div>
              <div class="tab-pane fade" id="ukelele-temario" role="tabpanel">
                <h4>Temario del Curso</h4>
                <div class="row">
                  <div class="col-md-6">
                    <h5>Básico</h5>
                    <ul>
                      <li>Conociendo tu ukelele</li>
                      <li>Acordes mayores y menores</li>
                      <li>Rasgueos básicos</li>
                      <li>Primeras canciones</li>
                    </ul>
                  </div>
                  <div class="col-md-6">
                    <h5>Intermedio</h5>
                    <ul>
                      <li>Acordes de séptima</li>
                      <li>Patrones rítmicos complejos</li>
                      <li>Introducción al fingerstyle</li>
                      <li>Transposición de canciones</li>
                    </ul>
                  </div>
                  <div class="col-md-6">
                    <h5>Avanzado</h5>
                    <ul>
                      <li>Técnicas solistas</li>
                      <li>Improvisación</li>
                      <li>Música hawaiana tradicional</li>
                      <li>Composición propia</li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="ukelele-instructor" role="tabpanel">
                <div class="row align-items-center">
                  <div class="col-md-4 text-center">
                    <img src="../assets/img/user.jpg" alt="Instructora Luisa Rodríguez" class="img-fluid rounded-circle mb-3" style="width: 150px; height: 150px; object-fit: cover;">
                    <h5>Luisa Rodríguez</h5>
                    <p class="text-muted">Instructora de Ukelele</p>
                  </div>
                  <div class="col-md-8">
                    <h4>Sobre la instructora</h4>
                    <p>Luisa es especialista en música hawaiana y contemporánea con el ukelele. Con más de 5 años de experiencia enseñando a niños y adultos, ha desarrollado un método único que hace el aprendizaje divertido y efectivo.</p>
                    <p>Su enfoque pedagógico se centra en la práctica inmediata y el disfrute de la música desde la primera clase.</p>
                    <div class="mt-3">
                      <span class="badge bg-primary me-1">Música Hawaiana</span>
                      <span class="badge bg-primary me-1">Fingerstyle</span>
                      <span class="badge bg-primary me-1">Enseñanza para Niños</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="text-center mt-4">
            <a href="#" class="btn btn-primary btn-lg" data-bs-toggle="modal" data-bs-target="#modalRegistro">Inscribirse al Curso</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal Requinto -->
  <div class="modal fade course-modal" id="requintoModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Curso de Requinto</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <img src="../assets/img/requinto.jpg" alt="Curso de requinto" class="course-details-img">
          
          <div class="course-tabs">
            <ul class="nav nav-tabs" id="requintoTab" role="tablist">
              <li class="nav-item" role="presentation">
                <button class="nav-link active" id="requinto-descripcion-tab" data-bs-toggle="tab" data-bs-target="#requinto-descripcion" type="button" role="tab">Descripción</button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link" id="requinto-temario-tab" data-bs-toggle="tab" data-bs-target="#requinto-temario" type="button" role="tab">Temario</button>
              </li>
              <li class="nav-item" role="presentation">
                <button class="nav-link" id="requinto-instructor-tab" data-bs-toggle="tab" data-bs-target="#requinto-instructor" type="button" role="tab">Instructor</button>
              </li>
            </ul>
            <div class="tab-content" id="requintoTabContent">
              <div class="tab-pane fade show active" id="requinto-descripcion" role="tabpanel">
                <h4>Descripción del Curso</h4>
                <p>Domina este instrumento melódico esencial en la música tradicional latinoamericana. En este curso aprenderás:</p>
                <ul class="course-features">
                  <li><i class="fas fa-check-circle"></i> Técnica de púa y digitación</li>
                  <li><i class="fas fa-check-circle"></i> Escalas y melodías tradicionales</li>
                  <li><i class="fas fa-check-circle"></i> Acompañamiento en diferentes ritmos</li>
                  <li><i class="fas fa-check-circle"></i> Improvisación melódica</li>
                  <li><i class="fas fa-check-circle"></i> Mantenimiento del instrumento</li>
                </ul>
              </div>
              <div class="tab-pane fade" id="requinto-temario" role="tabpanel">
                <h4>Temario del Curso</h4>
                <div class="accordion" id="requintoTemarioAccordion">
                  <div class="accordion-item">
                    <h3 class="accordion-header" id="requintoHeadingOne">
                      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#requintoCollapseOne" aria-expanded="true">
                        Fundamentos del Requinto
                      </button>
                    </h3>
                    <div id="requintoCollapseOne" class="accordion-collapse collapse show" aria-labelledby="requintoHeadingOne">
                      <div class="accordion-body">
                        <ul>
                          <li>Diferencias con la guitarra</li>
                          <li>Afinación y postura</li>
                          <li>Escalas básicas</li>
                          <li>Primeras melodías</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                  <div class="accordion-item">
                    <h3 class="accordion-header" id="requintoHeadingTwo">
                      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#requintoCollapseTwo">
                        Técnica Intermedia
                      </button>
                    </h3>
                    <div id="requintoCollapseTwo" class="accordion-collapse collapse" aria-labelledby="requintoHeadingTwo">
                      <div class="accordion-body">
                        <ul>
                          <li>Melodías tradicionales</li>
                          <li>Técnicas de púa avanzada</li>
                          <li>Armonización básica</li>
                          <li>Ritmos latinoamericanos</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                  <div class="accordion-item">
                    <h3 class="accordion-header" id="requintoHeadingThree">
                      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#requintoCollapseThree">
                        Avanzado y Estilos
                      </button>
                    </h3>
                    <div id="requintoCollapseThree" class="accordion-collapse collapse" aria-labelledby="requintoHeadingThree">
                      <div class="accordion-body">
                        <ul>
                          <li>Improvisación melódica</li>
                          <li>Técnicas solistas</li>
                          <li>Composición para requinto</li>
                          <li>Repertorio avanzado</li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="tab-pane fade" id="requinto-instructor" role="tabpanel">
                <div class="row align-items-center">
                  <div class="col-md-4 text-center">
                    <img src="../assets/img/user.jpg" alt="Instructor Carlos Méndez" class="img-fluid rounded-circle mb-3" style="width: 150px; height: 150px; object-fit: cover;">
                    <h5>Carlos Méndez</h5>
                    <p class="text-muted">Instructor de Requinto</p>
                  </div>
                  <div class="col-md-8">
                    <h4>Sobre el instructor</h4>
                    <p>Carlos es un experto en música tradicional y requinto con más de 15 años de experiencia. Ha participado en festivales internacionales de música folklórica y grabado con importantes agrupaciones de música latinoamericana.</p>
                    <p>Su enseñanza se centra en preservar las técnicas tradicionales mientras adapta el instrumento a contextos musicales contemporáneos.</p>
                    <div class="mt-3">
                      <span class="badge bg-primary me-1">Música Tradicional</span>
                      <span class="badge bg-primary me-1">Técnica de Púa</span>
                      <span class="badge bg-primary me-1">Improvisación</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="text-center mt-4">
            <a href="#" class="btn btn-primary btn-lg" data-bs-toggle="modal" data-bs-target="#modalRegistro">Inscribirse al Curso</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal Mensaje -->
  <div class="modal fade course-modal" id="messageModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Mensaje</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <p><?php echo htmlspecialchars($modalMessage); ?></p>
          
          <?php if(isset($_SESSION['password_errors'])): ?>
            <ul class="mt-3">
              <?php foreach($_SESSION['password_errors'] as $error): ?>
                <li><?php echo htmlspecialchars($error); ?></li>
              <?php endforeach; ?>
            </ul>
            <?php unset($_SESSION['password_errors']); ?>
          <?php endif; ?>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-primary" data-bs-dismiss="modal">Aceptar</button>
        </div>
      </div>
    </div>
  </div>
  
  <!-- Scripts -->
  <script src="../assets/js/index.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

  <?php if (!empty($modalMessage)): ?>
    <script>
      var myModal = new bootstrap.Modal(document.getElementById('messageModal'));
      myModal.show();
    </script>
  <?php endif; ?>

</body>
</html>