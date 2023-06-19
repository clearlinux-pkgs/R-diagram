#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-diagram
Version  : 1.6.5
Release  : 3
URL      : https://cran.r-project.org/src/contrib/diagram_1.6.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/diagram_1.6.5.tar.gz
Summary  : Functions for Visualising Simple Graphs (Networks), Plotting
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-shape
BuildRequires : R-shape
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
visualising webs, electrical networks, etc.
     Support for the book "A practical guide to ecological modelling -
     using R as a simulation platform"
     by Karline Soetaert and Peter M.J. Herman (2009), Springer.
     and the book "Solving Differential Equations in R"
     by Karline Soetaert, Jeff Cash and Francesca Mazzia (2012), Springer.
     Includes demo(flowchart), demo(plotmat), demo(plotweb).

%prep
%setup -q -n diagram

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680556545

%install
export SOURCE_DATE_EPOCH=1680556545
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/diagram/DESCRIPTION
/usr/lib64/R/library/diagram/INDEX
/usr/lib64/R/library/diagram/Meta/Rd.rds
/usr/lib64/R/library/diagram/Meta/data.rds
/usr/lib64/R/library/diagram/Meta/demo.rds
/usr/lib64/R/library/diagram/Meta/features.rds
/usr/lib64/R/library/diagram/Meta/hsearch.rds
/usr/lib64/R/library/diagram/Meta/links.rds
/usr/lib64/R/library/diagram/Meta/nsInfo.rds
/usr/lib64/R/library/diagram/Meta/package.rds
/usr/lib64/R/library/diagram/Meta/vignette.rds
/usr/lib64/R/library/diagram/NAMESPACE
/usr/lib64/R/library/diagram/R/diagram
/usr/lib64/R/library/diagram/R/diagram.rdb
/usr/lib64/R/library/diagram/R/diagram.rdx
/usr/lib64/R/library/diagram/data/Rdata.rdb
/usr/lib64/R/library/diagram/data/Rdata.rds
/usr/lib64/R/library/diagram/data/Rdata.rdx
/usr/lib64/R/library/diagram/demo/flowchart.r
/usr/lib64/R/library/diagram/demo/plotmat.r
/usr/lib64/R/library/diagram/demo/plotweb.r
/usr/lib64/R/library/diagram/doc/diagram.R
/usr/lib64/R/library/diagram/doc/diagram.Rnw
/usr/lib64/R/library/diagram/doc/diagram.pdf
/usr/lib64/R/library/diagram/doc/index.html
/usr/lib64/R/library/diagram/help/AnIndex
/usr/lib64/R/library/diagram/help/aliases.rds
/usr/lib64/R/library/diagram/help/diagram.rdb
/usr/lib64/R/library/diagram/help/diagram.rdx
/usr/lib64/R/library/diagram/help/paths.rds
/usr/lib64/R/library/diagram/html/00Index.html
/usr/lib64/R/library/diagram/html/R.css
